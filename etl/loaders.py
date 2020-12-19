from math import floor
from pathlib import Path

import collections
import pydotplus
from django.conf import settings
from django.utils import timezone
import numpy as np
import statsmodels.api as sm
from sklearn.base import is_classifier
from sklearn.linear_model import LinearRegression
from sklearn.tree import export_text, tree, _tree
from sklearn.tree._export import _compute_depth
from sklearn.utils.validation import check_is_fitted

from checklists.models.checklist.checklist_models import Checklist
from . import transformers

from sklearn import tree


def checklist_regr(*args, **kwargs):
    """
    https://www.statsmodels.org/stable/generated/statsmodels.regression.linear_model.RegressionResults.html
    """
    dvar = kwargs.get('dvar', 'count')
    building_features = kwargs.get('building_features', None)
    checklist_features = kwargs.get('checklist_features', None)

    checklists = []

    for cl in Checklist.objects.all():
        transformed = transformers.ChecklistTransformer(
            checklist=cl,
            building_features=building_features,
            checklist_features=checklist_features
        )

        # include checklist_rating
        transformed.independent['checklist_rating'] = cl.percentage_checklist_rating()

        # include avg_fire_rating
        transformed.independent['avg_fire_rating'] = transformed.building.avg_fire_rating()

        # include age
        age = (transformed.checklist.date_checked.date_obj - transformed.building.date_of_construction).days
        if age < 0:
            age = 0
        transformed.independent['building_age'] = age

        checklists.append(transformed)

    X = [ct.X for ct in checklists]

    if dvar == 'count':
        Y = [ct.dependent['incident_count'] > 0 for ct in checklists]
    else:
        Y = [ct.dependent[dvar] for ct in checklists]

    data_feature_names = checklists[0].X_labels()

    split = int(floor(len(X) * .7))
    train_X = np.array(X[:split])
    train_Y = np.array(Y[:split])
    test_X = np.array(X[split + 1:])
    test_Y = np.array(Y[split + 1:])

    train_X = sm.add_constant(train_X)

    model = sm.OLS(train_Y, train_X)

    result = model.fit()

    # predicted_Y = result.predict(test_X)

    return {
        'summary_html': result.summary().as_html(),
        'summary': result.summary().as_text(),
        'r2': result.rsquared,
        'r2_adj': result.rsquared_adj,
        'regression_coefficients': result.params,
        'result': result,
        'test_Y': test_Y,
        # 'predicted_Y': predicted_Y
    }


def checklist_dtree(*args, **kwargs):
    dvar = kwargs.get('dvar', 'has_incident')
    building_features = kwargs.get('building_features', None)
    checklist_features = kwargs.get('checklist_features', None)
    data = kwargs.get('checklists', None)
    checklists = []

    for cl in data:
        transformed = transformers.ChecklistTransformer(
            checklist=cl,
            building_features=building_features,
            checklist_features=checklist_features
        )

        # include checklist_rating
        transformed.independent['checklist_rating'] = cl.percentage_checklist_rating()

        # include avg_fire_rating
        transformed.independent['avg_fire_rating'] = transformed.building.avg_fire_rating()

        # include age
        age = (transformed.checklist.date_checked.date_obj - transformed.building.date_of_construction).days
        if age < 0:
            age = 0
        transformed.independent['building_age'] = age

        checklists.append(transformed)

    X = [ct.X for ct in checklists]

    if dvar == 'has_incident':
        Y = [ct.dependent['incident_count'] > 0 for ct in checklists]
    else:
        Y = [ct.dependent[dvar] for ct in checklists]

    data_feature_names = checklists[0].X_labels()
    classifier = tree.DecisionTreeClassifier()
    model = classifier.fit(X, Y)

    t = timezone.now().timestamp()

    fname = f"checklist_dtree--{t}.png"
    path = f"{settings.MEDIA_ROOT}models/trees"
    Path(path).mkdir(parents=True, exist_ok=True)

    dot_data = tree.export_graphviz(model,
                                    feature_names=data_feature_names,
                                    out_file=None,
                                    filled=True,
                                    rounded=True)
    graph = pydotplus.graph_from_dot_data(dot_data)

    colors = ('green', 'red')
    edges = collections.defaultdict(list)

    for edge in graph.get_edge_list():
        edges[edge.get_source()].append(int(edge.get_destination()))

    for edge in edges:
        edges[edge].sort()
        for i in range(2):
            dest = graph.get_node(str(edges[edge][i]))[0]
            dest.set_fillcolor(colors[i])

    graph.write_png(f"{path}/{fname}")
    code = tree_to_code(model, feature_names=list(data_feature_names))

    code_output = open(f"{settings.BASE_DIR}/dt_model.py", "w")
    code_output.write(code)
    code_output.close()

    return {
        "image": f"{settings.MEDIA_URL}models/trees/{fname}",
        "text": export_text(model, feature_names=list(data_feature_names))
    }


def tree_to_code(decision_tree, *, feature_names, max_depth=10, spacing=4, decimals=2, show_weights=False):
    """
    Ma generate ni sya sang dt_model.py na file sa root
    check mo lang dason
    """
    check_is_fitted(decision_tree)
    tree_ = decision_tree.tree_
    if is_classifier(decision_tree):
        class_names = decision_tree.classes_
    right_child_fmt = "{} {} <= {}\n"
    left_child_fmt = "{} {} >  {}\n"
    truncation_fmt = "{} {}\n"

    if max_depth < 0:
        raise ValueError("max_depth bust be >= 0, given %d" % max_depth)

    if (feature_names is not None and
            len(feature_names) != tree_.n_features):
        raise ValueError("feature_names must contain "
                         "%d elements, got %d" % (tree_.n_features,
                                                  len(feature_names)))

    if spacing <= 0:
        raise ValueError("spacing must be > 0, given %d" % spacing)

    if decimals < 0:
        raise ValueError("decimals must be >= 0, given %d" % decimals)

    if isinstance(decision_tree, tree.DecisionTreeClassifier):
        value_fmt = "{}{} weights: {}\n"
        if not show_weights:
            value_fmt = "{}{}{}\n"
    else:
        value_fmt = "{}{} value: {}\n"

    if feature_names:
        feature_names_ = [feature_names[i] if i != _tree.TREE_UNDEFINED
                          else None for i in tree_.feature]
    else:
        feature_names_ = ["feature_{}".format(i) for i in tree_.feature]

    export_text.report = "def eval_tree({}):\n".format(", ".join(feature_names))

    def _add_leaf(value, class_name, indent):
        val = ''
        is_classification = isinstance(decision_tree,
                                       tree.DecisionTreeClassifier)
        if show_weights or not is_classification:
            val = ["{1:.{0}f}, ".format(decimals, v) for v in value]
            val = '[' + ''.join(val)[:-2] + ']'
        if is_classification:
            val += ' result = ' + str(class_name)
        export_text.report += value_fmt.format(indent, '', val)

    def print_tree_recurse(node, depth):
        indent = (" " * spacing) * depth
        indent = indent[:-spacing] + " " * spacing

        value = None
        if tree_.n_outputs == 1:
            value = tree_.value[node][0]
        else:
            value = tree_.value[node].T[0]
        class_name = np.argmax(value)

        if (tree_.n_classes[0] != 1 and
                tree_.n_outputs == 1):
            class_name = class_names[class_name]

        if depth <= max_depth + 1:
            info_fmt = ""
            info_fmt_left = info_fmt
            info_fmt_right = info_fmt

            if tree_.feature[node] != _tree.TREE_UNDEFINED:
                name = f"if {feature_names_[node]}"
                threshold = tree_.threshold[node]
                threshold = "{1:.{0}f}:".format(decimals, threshold)
                export_text.report += right_child_fmt.format(indent,
                                                             name,
                                                             threshold)
                export_text.report += info_fmt_left
                print_tree_recurse(tree_.children_left[node], depth + 1)

                export_text.report += left_child_fmt.format(indent,
                                                            name,
                                                            threshold)
                export_text.report += info_fmt_right
                print_tree_recurse(tree_.children_right[node], depth + 1)
            else:  # leaf
                _add_leaf(value, class_name, indent)
        else:
            subtree_depth = _compute_depth(tree_, node)
            if subtree_depth == 1:
                _add_leaf(value, class_name, indent)
            else:
                trunc_report = 'pass'
                export_text.report += truncation_fmt.format(indent,
                                                            trunc_report)

    print_tree_recurse(0, 1)
    export_text.report += f"\n{' ' * spacing} return result"
    return export_text.report
