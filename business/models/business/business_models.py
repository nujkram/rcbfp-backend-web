"""
rcbfp Module
---
startup_ratings - Application Master Model 0.0.1
This is the Master model for Application
---
Author: Mark Gersaniva
Email: mark.gersaniva@springvalley.tech
"""
from django.contrib.postgres.forms import JSONField
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

from business.models.business.managers.business_managers import BusinessManager


class Business(models.Model):
    """
      The Business class defines the master data model for Business
      ## Fields
      **Basic**
      - created: DateTime
      - updated: DateTime

      **Identifiers**

      **Properties**

      **State**
      - active:bool
      - meta: JSON

      **Relationship Fields**
      - created_by: Account defined <em>defined in accounts.models</em>
      - last_updated_by: Account defined <em>defined in accounts.models</em>

      ## **Builtin methods**
      - __str__: returns a string representation of the object

      **Model overrides**
      - clean: exposed for placeholder of custom validation
      - save: auto-call full_clean() parent method

      **Model-specific methods**

      **Signals**
      - scaffold_post_save: post-save trigger
      - scaffold_pre_save: pre-save trigger

      """

    # === Basic ===
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    # === Identifiers ===

    # === Properties ===
    name = models.CharField(blank=False, max_length=254, null=False, unique=True)
    nature = models.CharField(blank=True, max_length=254, null=True)
    owner_first_name = models.CharField(blank=True, max_length=42, null=True)
    owner_middle_name = models.CharField(blank=True, max_length=42, null=True)
    owner_last_name = models.CharField(blank=True, max_length=42, null=True)
    address = models.CharField(max_length=254, blank=True, null=True)
    landline = models.CharField(max_length=16, blank=True, null=True)
    mobile_number = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(max_length=254, unique=True, verbose_name='email address')

    # === State ===
    active = models.BooleanField(default=True)
    meta = JSONField()

    # === Relationship Fields ===
    building = models.ForeignKey('buildings.Building', blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name='building_business')
    region = models.ForeignKey('locations.Region', blank=True, default=6, null=False, on_delete=models.CASCADE,
                               related_name='region_business')
    province = models.ForeignKey('locations.Province', blank=True, default=22, null=False, on_delete=models.CASCADE,
                                 related_name='province_business')
    city = models.ForeignKey('locations.City', blank=True, default=381, null=False, on_delete=models.CASCADE,
                             related_name='province_business')

    # Manager
    objects = BusinessManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = "Business"
        verbose_name_plural = "Businesses"
        unique_together = ('email',)

    ################################################################################
    # === Builtin methods ===
    ################################################################################
    def __str__(self):
        return self.name

    ################################################################################
    # === Model overrides ===
    ################################################################################
    def clean(self, *args, **kwargs):
        # add custom validation here
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        # self.full_clean()
        super().save(*args, **kwargs)

    ################################################################################
    # === Model-specific methods ===
    ################################################################################
    def get_full_name(self):
        if self.owner_first_name != '' and self.owner_last_name != '':
            return '{}, {}'.format(
                self.owner_last_name, self.owner_first_name
            )
        else:
            return 'Unnamed'

    ################################################################################
    # === Properties ===
    ################################################################################


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=Business)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=Business)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass
