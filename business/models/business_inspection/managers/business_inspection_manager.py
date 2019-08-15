from django.db import models
from django.apps import apps

class BusinessInspectionQuerySet(models.QuerySet):
  def actives(self):
    return self.filter(active=True)

class BusinessInspectionManager(models.Manager):
  def get_queryset(self):
    return BusinessInspectionQuerySet(self.model, using=self._db)

  def actives(self):
    return self.get_queryset().actives()