"""
rcbfp Module
---
buildings - Building Master Model 0.0.1
This is the Master model for Building
---
Author: Mark Gersaniva
Email: mark.gersaniva@springvalley.tech
"""

from django.contrib.postgres.forms import JSONField
from django.db import models
from django.apps import apps
from django.dispatch import receiver
from django_extensions.db import fields as extension_fields
from django.db.models.signals import post_save, pre_save

# Model manager
from buildings.models.building.managers.building_managers import BuildingManager


class Building(models.Model):
  """
  The Building class defines the master data model for Building
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
  name = models.CharField(max_length=120)
  slug = extension_fields.AutoSlugField(populate_from='name', blank=True)

  # === Properties ===
  address = models.CharField(max_length=120, blank=True, null=True)
  floor_number = models.PositiveSmallIntegerField(blank=True, null=True)
  height = models.FloatField(blank=True, null=True)
  floor_area = models.FloatField(blank=True, null=True)
  total_floor_area = models.FloatField(blank=True, null=True)
  beams = models.PositiveSmallIntegerField(blank=True, null=True)
  columns = models.PositiveSmallIntegerField(blank=True, null=True)
  flooring = models.FloatField(blank=True, null=True)
  exterior_walls = models.FloatField(blank=True, null=True)
  corridor_walls = models.FloatField(blank=True, null=True)
  room_partitions = models.PositiveSmallIntegerField(blank=True, null=True)
  main_stair = models.PositiveSmallIntegerField(blank=True, null=True)
  window = models.PositiveSmallIntegerField(blank=True, null=True)
  ceiling = models.PositiveSmallIntegerField(blank=True, null=True)
  main_door = models.PositiveSmallIntegerField(blank=True, null=True)
  trusses = models.PositiveSmallIntegerField(blank=True, null=True)
  roof = models.BooleanField()

  # === State ===
  active = models.BooleanField(default=True)
  meta = JSONField()

  # === Relationship Fields ===
  created_by = models.ForeignKey(
    'accounts.Account',
    on_delete=models.SET_NULL,
    null=True,
    db_index=False,
    related_name='created_buildings',
    blank=True
  )
  last_updated_by = models.ForeignKey(
    'accounts.Account',
    on_delete=models.SET_NULL,
    null=True,
    db_index=False,
    related_name='updated_buildings',
    blank=True
  )

  region = models.ForeignKey('locations.Region', on_delete=models.SET_NULL, null=True, related_name='region_building',
                             blank=True)
  province = models.ForeignKey('locations.Province', on_delete=models.SET_NULL, null=True,
                               related_name='province_building', blank=True)
  city = models.ForeignKey('locations.City', on_delete=models.SET_NULL, null=True, related_name='city_building',
                           blank=True)

  # Manager
  objects = BuildingManager

  class Meta:
    ordering = ('name',)
    verbose_name = "Building"
    verbose_name_plural = "Buildings"

  ################################################################################
  # === Builtin methods ===
  ################################################################################
  def __str__(self):
    return f'{self.name}'

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
@receiver(post_save, sender=Building)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
  pass


@receiver(pre_save, sender=Building)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
  pass
