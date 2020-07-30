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
from django.db import models, IntegrityError
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import datetime, timedelta, time

from business.models import Business
from business.models.business_application.managers.business_application_managers import BusinessApplicationManager


class BusinessApplication(models.Model):
    """
      The BusinessApplication class defines the master data model for BusinessApplication
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
    first_name = models.CharField(blank=True, max_length=42, null=True)
    middle_name = models.CharField(blank=True, max_length=42, null=True)
    last_name = models.CharField(blank=True, max_length=42, null=True)
    email = models.EmailField(max_length=254, verbose_name='email address')

    # === State ===
    approved = models.BooleanField(default=False)
    meta = JSONField()

    # === Relationship Fields ===
    business = models.ForeignKey('business.Business', on_delete=models.CASCADE, related_name='business_application')
    date_approved = models.ForeignKey('datesdim.DateDim', blank=True, null=True, on_delete=models.CASCADE,
                                      related_name='datetime_approved')

    # Manager
    objects = BusinessApplicationManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = "Business Application"
        verbose_name_plural = "Business Applications"

    ################################################################################
    # === Builtin methods ===
    ################################################################################
    def __str__(self):
        return f'{self.business} - {self.first_name}'

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
        if self.first_name != '' and self.last_name != '':
            return '{}, {}'.format(
                self.last_name, self.first_name
            )
        else:
            return 'Unnamed'
    ################################################################################
    # === Properties ===
    ################################################################################


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=BusinessApplication)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=BusinessApplication)
def scaffold_pre_save(sender, instance, created=False, **kwargs):
    year = datetime.now().year
    if created:
        if BusinessApplication.objects.filter(business=instance.business, approved=True,
                                              created__range=[f'{year}-01-01 00:00:00',
                                                              f'{year}-12-31 00:00:00']).count() > 0:
            raise IntegrityError("Business Application already approved!")
        elif BusinessApplication.objects.filter(business=instance.business, approved=False,
                                                created__range=[f'{year}-01-01 00:00:00',
                                                                f'{year}-12-31 00:00:00']).count() > 0:
            raise IntegrityError("Business Application already submitted! Please wait for schedule of inspection")
