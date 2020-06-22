from typing import Dict, Union, List

from buildings.models.building.building_models import Building
from business.models import Business
from checklists.models.checklist.checklist_models import Checklist
from etl.utils.transformer_utils import process_independents, process_dependents
from incidents.models.incident.incident_models import Incident


class ChecklistTransformer:
    independent: Dict = {}
    dependent: Dict = {}

    checklist: Checklist = None
    building: Building = None
    business: Business = None
    incidents: Union[List, Incident] = None

    numeric_only: bool = True
    force_int: bool = True

    building_features: List = None
    checklist_features: List = None

    @property
    def X(self) -> List:
        return self._X()

    def __init__(self, checklist: Checklist, building_features: List = None, checklist_features: List = None):
        self.checklist = checklist
        self.building = checklist.building
        self.business = checklist.business

        if building_features:
            self.building_features = building_features
        else:
            self.building_features = self.building.analytics_features

        if checklist_features:
            self.checklist_features = checklist_features
        else:
            self.checklist_features = self.checklist.analytics_features

        self.independent = {
            **process_independents(
                obj=self.building,
                analytics_features=self.building_features,
                numeric_only=self.numeric_only, force_int=self.force_int),
            **process_independents(
                obj=self.checklist,
                analytics_features=self.checklist_features,
                numeric_only=self.numeric_only, force_int=self.force_int)
        }

        self.incidents = Incident.objects.filter(
            building=self.building,
            business=self.business,
            occurrence__year=self.checklist.date_checked.year
        )

        self.dependent = process_dependents(self.incidents)

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
