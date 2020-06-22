from typing import Dict, Union, List

from incidents.models.incident.incident_models import Incident


def analyze_feature(feature, numeric_only: bool = True, force_int: bool = True):
    if numeric_only:
        allowed_field_types = [
            int,
            float,
            bool,
        ]
    else:
        allowed_field_types = []

    if len(allowed_field_types) > 0:
        if type(feature) not in allowed_field_types:
            return None

    if force_int:
        try:
            feature = int(feature)
        except TypeError:
            pass

    return feature


def process_independents(obj: object, analytics_features: Dict, numeric_only: bool = True, force_int: bool = True):
    data = {}
    for feature in analytics_features:
        f = analyze_feature(getattr(obj, feature), numeric_only, force_int)

        if f is not None:
            data[feature] = f
    return data


def process_dependents(incidents: Union[List, Incident]):
    totals = {
        'incident_count': incidents.count()
    }
    for feature in Incident.analytics_features:
        totals[feature] = 0

    for incident in incidents:
        for feature in Incident.analytics_features:
            totals[feature] += getattr(incident, feature)

    return totals
