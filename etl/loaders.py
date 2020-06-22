from math import floor
from pathlib import Path

import collections
import pydotplus
from django.conf import settings
from django.utils import timezone
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.tree import export_text

from checklists.models.checklist.checklist_models import Checklist
from . import transformers

from sklearn import tree


def checklist_regr(*args, **kwargs):
    dvar = kwargs.get('dvar', 'count')

    checklists = []

    for cl in Checklist.objects.all():
        transformed = transformers.ChecklistTransformer(cl)

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
    train_X = X[:split]
    train_Y = Y[:split]
    test_X = X[split + 1:]
    test_Y = Y[split + 1:]

    classifier = LinearRegression()
    model = classifier.fit(train_X, train_Y)

    prediction_y = model.predict(test_X)

    return {
        'model': model,
        'score': model.score(train_X, train_Y),
        'intercept': model.intercept_,
        'slope': model.coef_,
        'prediction_slope': model.intercept_ + np.sum(model.coef_ * train_X, axis=1),
        'prediction': prediction_y,
        'test_X': test_X,
        'test_Y': test_Y
    }


def checklist_dtree(*args, **kwargs):
    dvar = kwargs.get('dvar', 'count')

    checklists = []

    for cl in Checklist.objects.all():
        transformed = transformers.ChecklistTransformer(cl)

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

    graph.write(f"{path}/{fname}")

    return (
        f"{settings.MEDIA_URL}models/trees/{fname}",
        export_text(model, feature_names=list(data_feature_names))
    )
