from django.db import models
from django.apps import apps


class IncidentQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class IncidentManager(models.Manager):
    def get_queryset(self):
        return IncidentQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()
