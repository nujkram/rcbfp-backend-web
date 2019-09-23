from django.db import models
from django.apps import apps


class ChecklistQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class ChecklistManager(models.Manager):
    def get_queryset(self):
        return ChecklistQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()
