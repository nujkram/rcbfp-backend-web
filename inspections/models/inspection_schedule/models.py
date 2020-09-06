"""
RCBFP Project
Inspection 0.0.1
Inspection Schedule models
Inspection Schedule

Author: Mark
"""

import uuid as uuid
from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields
from django.apps import apps
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.contrib.postgres.fields import JSONField

from inspections.constants import STATUS_CHOICES, INSPECTION_TYPE_CHOICES
from inspections.models.inspection_schedule.managers.inspection_managers import InspectionScheduleManager


class InspectionSchedule(models.Model):
    # === Basic ===
    created = models.DateTimeField(null=False, auto_now_add=True)
    updated = models.DateTimeField(null=False, auto_now=True)

    # === Identifiers ===
    inspection_date = models.DateField(null=False, blank=False)

    # === Properties ===

    # === State ===
    active = models.BooleanField(default=True)
    meta = JSONField(default=dict, blank=True, null=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=False, null=False, default=1)
    inspection_type = models.PositiveSmallIntegerField(choices=INSPECTION_TYPE_CHOICES, blank=False, null=False, default=1)

    # === Relationship Fields ===
    user = models.ForeignKey(
        'accounts.Account', blank=True, null=True, on_delete=models.SET_NULL, related_name='user_inspection'
    )
    building = models.ForeignKey('buildings.Building', blank=True, null=True, on_delete=models.CASCADE,
                                 related_name='building_inspection')
    business = models.ForeignKey('business.Business', blank=True, null=True, on_delete=models.CASCADE,
                                 related_name='building_inspection')

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='inspection_schedules_created_by_user'
    )
    last_updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        db_index=False,
        on_delete=models.SET_NULL,
        related_name='inspection_schedules_updated_by_user'
    )

    objects = InspectionScheduleManager()

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Inspection Schedule'
        verbose_name_plural = 'Inspection Schedules'

    ################################################################################
    # === Magic Methods ===
    ################################################################################
    def __str__(self):
        return f'{self.building} - {self.business}'

        ################################################################################

    # === Model overrides ===
    ################################################################################
    def clean(self, *args, **kwargs):
        # add custom validation here
        super().clean()

    def save(self, *args, **kwargs):
        # self.full_clean()
        super().save(*args, **kwargs)

    ################################################################################
    # === Model-specific methods ===
    ################################################################################


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=InspectionSchedule)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=InspectionSchedule)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass
