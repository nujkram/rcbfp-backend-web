import datetime

import dateutil
import phonenumbers
from django.db import models
from django_extensions.db import fields as extension_fields
from phonenumber_field.modelfields import PhoneNumberField

from profiles.constants import MARITAL_STATUS_CHOICES, RANK, MOBTEL_CARRIERS
from profiles.managers import BaseProfileManager


class Gender(models.Model):
    name = models.CharField(max_length=32)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

    created = models.DateTimeField(null=False, auto_now_add=True)
    last_updated = models.DateTimeField(null=False, auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class BaseProfile(models.Model):
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    middle_name = models.CharField(max_length=60, blank=True, null=True)

    date_of_birth = models.DateField(null=True, blank=True)
    marital_status = models.CharField(choices=MARITAL_STATUS_CHOICES, default="I'd rather not say", max_length=60,
                                      blank=True, null=True)
    rank = models.CharField(choices=RANK, default='Fire Officer 1', max_length=32, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    created = models.DateTimeField(null=False, auto_now_add=True)
    last_updated = models.DateTimeField(null=False, auto_now=True)

    # Relationship Fields
    gender = models.ForeignKey(Gender, related_name='gender_profile', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey('accounts.Account', related_name='account_profiles', on_delete=models.CASCADE)

    objects = BaseProfileManager()

    class Meta:
        ordering = ('user', '-created')

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.user.email

    def get_midlle_initial(self):
        if self.middle_name:
            return self.middle_name[0].upper()
        else:
            return ''

    def get_age(self):
        today = datetime.datetime.utcnow()
        today = today.date()
        age = dateutil.relativedelta.relativedelta(today, self.date_of_birth)
        age = age.years
        return age


class ProfileMobtel(models.Model):
    number = PhoneNumberField(unique=True)
    carrier = models.PositiveSmallIntegerField(choices=MOBTEL_CARRIERS)
    is_public = models.BooleanField(default=False)
    is_primary = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    created = models.DateTimeField(null=False, auto_now_add=True)
    last_updated = models.DateTimeField(null=False, auto_now=True)

    # Relationship Fields
    profile = models.ForeignKey(BaseProfile, related_name='profile_mobtels', on_delete=models.CASCADE)

    class Meta:
        ordering = ('number', '-created')

    def __str__(self):
        return f'{self.number}'

    def is_valid(self):
        return phonenumbers.is_valid_number(self)


class ProfileAddress(models.Model):
    address1 = models.CharField(
        "Address line 1",
        max_length=1024,
    )

    address2 = models.CharField(
        "Address line 2",
        max_length=1024
    )

    zip_code = models.CharField(
        "ZIP / Postal code",
        max_length=12,
    )

    city = models.CharField(
        'City / Municipality',
        max_length=1024,
    )

    country = models.ForeignKey('locations.Country', related_name='country_addresses', on_delete=models.CASCADE)

    # Relationship Fields
    profile = models.ForeignKey(BaseProfile, related_name='profile_addresses', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Address'
        verbose_name_plural = 'Addresses'

    def __str__(self):
        return  self.address1

    def as_html(self):
        return "<p>{}<br>{}</p><p>{}, {}, {}".format(
            self.address1,
            self.address2,
            self.city,
            self.country,
            self.zip_code
        )