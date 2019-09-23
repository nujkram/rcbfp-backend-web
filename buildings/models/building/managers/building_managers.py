from django.db import models
from django.apps import apps


class BuildingQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class BuildingManager(models.Manager):
    def get_queryset(self):
        return BuildingQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()
