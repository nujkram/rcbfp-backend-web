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

from business.models.business_evaluation.managers.business_evaluation_managers import BusinessEvaluationManager


class BusinessEvaluation(models.Model):
  """
    The BusinessEvaluation class defines the master data model for BusinessEvaluation
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
  architectural = models.BooleanField(default=False)
  structural = models.BooleanField(default=False)
  electrical = models.BooleanField(default=False)
  mechanical = models.BooleanField(default=False)
  license_of_involved_professional = models.BooleanField(default=False)
  plumbing = models.BooleanField(default=False)
  electronics = models.BooleanField(default=False)
  sanitary = models.BooleanField(default=False)
  fire_protection_plan = models.BooleanField(default=False)
  estimated_cost = models.BooleanField(default=False)

  # === State ===
  approved = models.BooleanField(default=False)
  meta = JSONField()

  # === Relationship Fields ===
  business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='business_evaluation')
  date_evaluated = models.ForeignKey('datesdim.DateDim', blank=True, null=True, on_delete=models.CASCADE, related_name='datetime_evaluated')

  # Manager
  objects = BusinessEvaluationManager()

  class Meta:
    ordering = ('-created',)
    verbose_name = "Business Evaluation"
    verbose_name_plural = "Business Evaluations"

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
@receiver(post_save, sender=BusinessEvaluation)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
  pass


@receiver(pre_save, sender=BusinessEvaluation)
def scaffold_pre_save(sender, instance, created=False, **kwargs):
  pass