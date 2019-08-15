from django.db import models
from django.apps import apps


class BusinessApplicationQuerySet(models.QuerySet):
  def actives(self):
    return self.filter(active=True)


class BusinessApplicationManager(models.Manager):
  def get_queryset(self):
    return BusinessApplicationQuerySet(self.model, using=self._db)

  def actives(self):
    return self.get_queryset().actives()
