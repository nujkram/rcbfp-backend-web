from django.db import models
from django.apps import apps

from buildings.models.building.building_models import Building
from locations.models import Region, Province, City


class BusinessQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class BusinessManager(models.Manager):
    def get_queryset(self):
        return BusinessQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def create(self, *args, **kwargs):
        flag = True
        m = []

        try:
            building = Building.objects.get(name=kwargs['building'])
        except Building.DoesNotExist:
            flag = False
            m.append(f'{building} is an invalid region')

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
            business = self.model(
                name=kwargs['name'],
                nature=kwargs['nature'],
                owner_first_name=kwargs['owner_first_name'],
                owner_middle_name=kwargs['owner_middle_name'],
                owner_last_name=kwargs['owner_last_name'],
                address=kwargs['address'],
                landline=kwargs['landline'],
                mobile_number=kwargs['mobile_number'],
                email=kwargs['email'],
                building=kwargs['building'],
                region=kwargs['region'],
                province=kwargs['province'],
                city=kwargs['city'],
            )
            business.save()
            return business, 'Business recorded!'
        else:
            return False, m
