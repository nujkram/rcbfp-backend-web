from django.db import models
from django.apps import apps

class BusinessQuerySet(models.QuerySet):
  def actives(self):
    return self.filter(active=True)

class BusinessManager(models.Manager):
  def get_queryset(self):
    return BusinessQuerySet(self.model, using=self._db)

  def actives(self):
    return self.get_queryset().actives()