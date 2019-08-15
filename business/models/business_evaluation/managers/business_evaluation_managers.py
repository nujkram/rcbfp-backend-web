from django.db import models
from django.apps import apps

class BusinessEvaluationQuerySet(models.QuerySet):
  def actives(self):
    return self.filter(active=True)

class BusinessEvaluationManager(models.Manager):
  def get_queryset(self):
    return BusinessEvaluationQuerySet(self.model, using=self._db)

  def actives(self):
    return self.get_queryset().actives()