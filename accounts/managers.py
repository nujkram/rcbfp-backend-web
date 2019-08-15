from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models
from django.utils.text import slugify

from accounts.constants import INSPECTOR, ADMIN, SUPERADMIN


class AccountProviderManager(models.Manager):
    def create_user(self, **kwargs):
        pass


class AccountQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(is_active=True)

    def admins(self):
        return self.filter(user_type=ADMIN)

    def inspectors(self):
        return self.filter(user_type=INSPECTOR)


class AccountManager(BaseUserManager):
    def get_queryset(self):
        return AccountQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def admins(self):
        return self.get_queryset().admins()

    def inspectors(self):
        return self.get_queryset().inspectors()

    def create_user(self, email, username=None, password=None, user_type=None):
        email_validator = EmailValidator()
        try:
            email_validator(email)
            if not username:
                username = slugify(email)
            user = self.model(
                username=username,
                email=self.normalize_email(email),
                user_type=user_type,
            )

            user.set_password(password)
            user.save(using=self._db)
            user.regenerate_hash()
            return user
        except ValidationError:
            return False

    def create_superuser(self, email, password, username=None):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
        )
        user.user_type = SUPERADMIN
        user.is_admin = True
        user.save(using=self._db)
        return user