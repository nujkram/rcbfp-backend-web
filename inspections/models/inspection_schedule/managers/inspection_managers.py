from django.db import models
from django.apps import apps

from accounts.models import Account
from buildings.models.building.building_models import Building
from business.models import Business


class InspectionScheduleQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class InspectionScheduleManager(models.Manager):
    def get_queryset(self):
        return InspectionScheduleQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def create(self, *args, **kwargs):
        flag = True
        m = []
        date = kwargs['inspection_date']
        account = kwargs['user']
        inspection_type = kwargs['inspection_type']
        building = kwargs['building']
        business = kwargs['business']
        print(inspection_type)
        if date:
            for data in date:
                inspection_date = data

        if account:
            for data in account:
                username = data
        try:
            user = Account.objects.get(username=username)
        except Account.DoesNotExist:
            flag = False
            m.append(f'{user} does not exists!')

        try:
            building = Building.objects.get(name=building[0])
        except Building.DoesNotExist:
            flag = False
            m.append(f'{building} does not exists!')

        try:
            business = Business.objects.get(name=business[0])
        except Business.DoesNotExist:
            flag = False
            m.append(f'{business} does not exists!')

        if flag:
            inspection = self.model(
                inspection_date=inspection_date,
                user=user,
                inspection_type=inspection_type,
                building=building,
                business=business,
            )
            inspection.save()
            return inspection, 'Inspection recorded!'
        else:
            return False, m
