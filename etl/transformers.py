from typing import Dict, Union, List

import datetime

from buildings.models.building.building_models import Building
from business.models import Business
from checklists.models.checklist.checklist_models import Checklist
from incidents.models.incident.incident_models import Incident


class ChecklistTransformer:
    independent: Dict = {}
    dependent: Dict = {}

    checklist: Checklist = None
    building: Building = None
    business: Business = None
    incidents: Union[List, Incident] = None

    @property
    def X(self) -> List:
        return self._X()

    def __init__(self, checklist: Checklist):
        self.checklist = checklist
        self.building = checklist.building
        self.business = checklist.business

        self.independent = {
            **self.process_independents(self.building, self.building.analytics_features),
            **self.process_independents(self.checklist, self.checklist.analytics_features)
        }

        self.incidents = Incident.objects.filter(
            building=self.building,
            business=self.business,
            occurrence__year=self.checklist.date_checked.year
        )

        self.dependent = self.process_dependents()

    @staticmethod
    def analyze_feature(feature: object):
        if isinstance(feature, str):
            return None

        if isinstance(feature, datetime.time):
            return None

        if isinstance(feature, datetime.date):
            return feature.month

        if isinstance(feature, bool):
            return int(feature)

        return feature

    def process_independents(self, obj: object, analytics_features: Dict):
        data = {}
        for feature in analytics_features:
            f = self.analyze_feature(getattr(obj, feature))

            if f is not None:
                data[feature] = f
        return data

    def process_dependents(self):
        totals = {
            'incident_count': self.incidents.count()
        }
        for feature in Incident.analytics_features:
            totals[feature] = 0

        for incident in self.incidents:
            for feature in Incident.analytics_features:
                totals[feature] += getattr(incident, feature)

        return totals

    def _X(self):
        data = []
        for key, value in self.independent.items():
            data.append(value)

        return data

    def X_labels(self):
        data = []
        for key, value in self.independent.items():
            data.append(key)

        return data
