from django.db import models

from accounts.constants import INSPECTOR, ADMIN


class BaseProfileQuerySet(models.QuerySet):
    def providers(self):
        return self.user.filter(user_type=ADMIN)

    def users(self):
        return self.user.filter(user_type=INSPECTOR)

class BaseProfileManager(models.Manager):
    def get_queryset(self):
        return BaseProfileQuerySet(self.model, using=self._db)

    def providers(self):
        return self.get_queryset().providers()

    def users(self):
        return self.get_queryset().users

    def create(self, *args, **kwargs):
        try:
            user = self.model.objects.get(user=kwargs['user'])
            return user
        except self.model.DoesNotExist:
            return super(BaseProfileManager, self).create(*args, **kwargs)
