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

    @property
    def X(self) -> List:
        return self._X()

    def __init__(self, checklist: Checklist):
        self.checklist = checklist
        self.building = checklist.building
        self.business = checklist.business

        self.independent = {
            **process_independents(
                obj=self.building,
                analytics_features=self.building.analytics_features,
                numeric_only=self.numeric_only, force_int=self.force_int),
            **process_independents(
                obj=self.checklist,
                analytics_features=self.checklist.analytics_features,
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
