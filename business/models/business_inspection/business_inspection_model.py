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

from business.models.business_inspection.managers.business_inspection_manager import BusinessInspectionManager


class BusinessInspection(models.Model):
  """
    The BusinessInspectionDocument class defines the master data model for BusinessInspectionDocument
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
  occupancy_certificate = models.BooleanField(default=False)
  completion_certificate = models.BooleanField(default=False)
  built_plan = models.BooleanField(default=False)
  business_permit_form = models.BooleanField(default=False)
  fire_insurance = models.BooleanField(default=False)
  building_alteration = models.BooleanField(default=False)

  # === State ===
  approved = models.BooleanField(default=True)
  meta = JSONField()

  # === Relationship Fields ===
  business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='business_inspection')
  date_inspected = models.ForeignKey('datesdim.DateDim', blank=True, null=True, on_delete=models.CASCADE, related_name='datetime_inspection')

  # Manager
  objects = BusinessInspectionManager

  class Meta:
    ordering = ('-created',)
    verbose_name = "Business Inspection"
    verbose_name_plural = "Business Inspections"

  ################################################################################
  # === Builtin methods ===
  ################################################################################
  def __str__(self):
    return self.business.name

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

  ################################################################################
  # === Properties ===
  ################################################################################


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=BusinessInspection)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
  pass


@receiver(pre_save, sender=BusinessInspection)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
  pass
