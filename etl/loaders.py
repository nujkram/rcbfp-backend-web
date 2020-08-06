from math import floor
from pathlib import Path

import collections
import pydotplus
from django.conf import settings
from django.utils import timezone
import numpy as np
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.tree import export_text, _tree

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

    return {
        "image": f"{settings.MEDIA_URL}models/trees/{fname}",
        "text": export_text(model, feature_names=list(data_feature_names))
    }


def tree_to_code(*args, **kwargs):
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
    classifier = tree.DecisionTreeClassifier(criterion='entropy')  # tree

    # model = classifier.fit(X, Y)
    classifier.fit(X, Y)

    tree_ = classifier.tree_
    feature_names = list(checklists)

    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    def recurse(node, depth):
        indent = " " * depth
        print(f"feature {tree_.feature[node]}")
        print(f"undefined {_tree.TREE_UNDEFINED}")

        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]

            print("{}if {} <= {}:".format(indent, name, threshold))
            recurse(tree_.children_left[node], depth + 1)
            print("{}else:  # if {} > {}".format(indent, name, threshold))
            recurse(tree_.children_right[node], depth + 1)
        else:
            print("{}return asdasdsad {}".format(indent, tree_.value[node]))

    return recurse(0, 1)

# from etl import loaders
# building = Building.objects.first()
# building_features = building.analytics_features
# checklist = Checklist.objects.first()
# checklist_features = checklist.analytics_features
# checklists = Checklist.objects.filter(building=building)
# loaders.tree_to_code(building_features=building_features, checklist_features=checklist_features, checklists=checklists)
