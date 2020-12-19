from django.db import models
from django.apps import apps

from buildings.models.building.building_models import Building
from business.models import Business
from datesdim.models import DateDim
from locations.models import Region, Province, City


class IncidentQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class IncidentManager(models.Manager):
    def get_queryset(self):
        return IncidentQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def create(self, *args, **kwargs):
        flag = True
        m = []

        try:
            building = Building.objects.get(name=kwargs['building'])
        except Building.DoesNotExist:
            flag = False
            m.append(f'{building} is an invalid building')

        try:
            business = Business.objects.get(name=kwargs['business'])
        except Business.DoesNotExist:
            flag = False
            m.append(f'{business} is an invalid business')

        try:
            region = Region.objects.get(name=kwargs['region'])
        except Region.DoesNotExist:
            flag = False
            m.append(f'{region} is an invalid region')

        try:
            province = Province.objects.get(name=kwargs['province'])
        except Province.DoesNotExist:
            flag = False
            m.append(f'{province} is an invalid province')

        try:
            city = City.objects.get(name=kwargs['city'])
        except City.DoesNotExist:
            flag = False
            m.append(f'{city} is an invalid city')

        if flag:
            incident = self.model(
                first_name=kwargs['first_name'],
                last_name=kwargs['last_name'],
                middle_name=kwargs['middle_name'],
                phone=kwargs['phone'],
                address=kwargs['address'],
                image=kwargs['image'],
                incident_type=kwargs['incident_type'],
                property_damage=kwargs['property_damage'],
                casualties=kwargs['casualties'],
                major_injuries=kwargs['major_injuries'],
                minor_injuries=kwargs['minor_injuries'],
                intensity=kwargs['intensity'],
                severity=kwargs['severity'],
                duration=kwargs['duration'],
                building=kwargs['building'],
                business=kwargs['business'],
                region=kwargs['region'],
                province=kwargs['province'],
                city=kwargs['city'],
                occurrence=kwargs['occurrence'],
            )

            incident.save()
            return incident, 'Incident recorded!'
        else:
            return False, m
