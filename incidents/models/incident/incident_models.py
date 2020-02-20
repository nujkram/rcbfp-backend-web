"""
rcbfp Module
---
incidents - Incident Master Model 0.0.1
This is the Master model for Incident
---
Author: Mark Gersaniva
Email: mark.gersaniva@springvalley.tech
"""

import uuid
from django.contrib.postgres.forms import JSONField
from django.db import models
from django.apps import apps
from django.dispatch import receiver
from django_extensions.db import fields as extension_fields
from django.db.models.signals import post_save, pre_save

# Model manager
from incidents.constants import INCIDENT_TYPE_CHOICES
from incidents.models.incident.managers.incident_managers import IncidentManager


def photo_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'uploads/incident_photos/{filename}'


class Incident(models.Model):
    """
    The Incident class defines the master data model for Incident
    ## Fields
    **Basic**
    - created: DateTime
    - updated: DateTime

    **Identifiers**
    - name: Char(120)
    - slug: auto from name

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
    first_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(max_length=60, blank=True, null=True)
    middle_name = models.CharField(max_length=60, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    address = models.CharField(max_length=1024)
    image = models.ImageField(upload_to=photo_upload_path, max_length=512, blank=True, null=True)
    incident_type = models.CharField(choices=INCIDENT_TYPE_CHOICES, max_length=50, blank=False, null=False)

    # === State ===
    meta = JSONField()

    # === Relationship Fields ===
    building = models.ForeignKey(
        'buildings.Building',
        blank=True,
        null=True,
        related_name='incident_building',
        on_delete=models.SET_NULL
    )
    business = models.ForeignKey(
        'business.Business',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='incident_business'
    )
    region = models.ForeignKey(
        'locations.Region',
        blank=True,
        null=False,
        default=6,
        related_name='incident_region',
        on_delete=models.CASCADE
    )
    province = models.ForeignKey(
        'locations.Province',
        blank=True,
        null=False,
        default=4,
        related_name='incident_province',
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        'locations.City',
        blank=True,
        null=False,
        related_name='incident_city',
        on_delete=models.CASCADE
    )

    occurrence = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='incident_datetime'
    )

    created_by = models.ForeignKey(
        'accounts.Account',
        on_delete=models.SET_NULL,
        null=True,
        db_index=False,
        related_name='created_incidents',
        blank=True
    )
    last_updated_by = models.ForeignKey(
        'accounts.Account',
        on_delete=models.SET_NULL,
        null=True,
        db_index=False,
        related_name='updated_incidents',
        blank=True
    )

    # Manager
    objects = IncidentManager()

    class Meta:
        ordering = ('first_name',)
        verbose_name = "Incident"
        verbose_name_plural = "Incidents"

    ################################################################################
    # === Builtin methods ===
    ################################################################################
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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
# === Signals ===
################################################################################
@receiver(post_save, sender=Incident)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=Incident)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass


class IncidentCoordinate(models.Model):
    lat = models.DecimalField(max_digits=20, decimal_places=16, null=True, blank=True)
    lng = models.DecimalField(max_digits=20, decimal_places=16, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False, null=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False, null=False)

    incident = models.ForeignKey(Incident, on_delete=models.CASCADE, related_name='incident_coordinates')

    class Meta:
        ordering = ('-created',)
        unique_together = ('lat', 'lng', 'incident',)

    def __str__(self):
        return f'{self.lat}, {self.lng}'
