import datetime
import uuid

import hashlib

from django.contrib.auth.models import (
    AbstractBaseUser
)
from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django_extensions.db import fields as extension_fields

from accounts.constants import USERNAME_REGEX, USER_TYPE_CHOICES, INSPECTOR
from accounts.managers import AccountManager, AccountProviderManager
from profiles.models import BaseProfile

class AccountProvider(models.Model):
    name = models.CharField(max_length=254)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    domain = models.URLField()
    api_key = models.UUIDField(default=uuid.uuid4, editable=False)

    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(null=False, auto_now_add=True)
    last_updated = models.DateTimeField(null=False, auto_now=True)

    objects = AccountProviderManager()

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return f'{self.name} ({self.domain})'

    def get_users(self):
        rel = self.accountprovider_providers.filter(is_active=True)
        return [r.account for r in rel]


class Account(AbstractBaseUser):
    username = models.CharField(
        max_length=1024,
        validators=[
            RegexValidator(
                regex=USERNAME_REGEX,
                message='Username can only contain alphanumeric characters and the following characters: . -',
                code='Invalid Username'
            )
        ],
        unique=False
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=254,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=INSPECTOR, null=True, blank=True)
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    hash = models.CharField(null=True, blank=True, editable=False, max_length=254)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    def base_profile(self):
        return self.account_profiles.all().first()

    def nicename(self):
        profile = self.base_profile()
        if profile.last_name and profile.first_name:
            return f'{profile.first_name} {profile.last_name}'
        else:
            return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    def regenerate_hash(self):
        hash = hashlib.sha1(str(datetime.datetime.now()).encode('utf-8')).hexdigest()
        self.hash = hash
        self.save()

    class Meta:
        ordering = ('-created',)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class AccountProviderUser(models.Model):
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    # Relationship Fields
    account = models.ForeignKey(Account, related_name='accountprovider_users', on_delete=models.CASCADE)
    account_provider = models.ForeignKey(AccountProvider, related_name='accountprovider_providers',
                                         on_delete=models.CASCADE)

    class Meta:
        ordering = ('account_provider',)
        unique_together = ('account', 'account_provider')

    def __str__(self):
        return f'{self.account} on {self.account_provider}'


@receiver(post_save, sender=Account)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


@receiver(post_save, sender=Account)
def create_base_profile(sender, instance=None, created=False, **kwargs):
    if created:
        BaseProfile.objects.create(user=instance)