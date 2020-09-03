"""
rcbfp Module
---
buildings - Building Master Model 0.0.1
This is the Master model for Building
---
Author: Mark Gersaniva
Email: mark.gersaniva@springvalley.tech
"""
from datetime import date

from django.contrib.postgres.forms import JSONField
from django.db import models
from django.apps import apps
from django.dispatch import receiver
from django_extensions.db import fields as extension_fields
from django.db.models.signals import post_save, pre_save
from sklearn.tree import _tree
import dt_model

# Model manager
from buildings.constants import BUILDING_STATUS_CHOICES
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
    latitude = models.CharField(max_length=24, blank=True, null=True)
    longitude = models.CharField(max_length=24, blank=True, null=True)

    # features
    date_of_construction = models.DateField(null=True, blank=True)
    floor_number = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.FloatField(blank=True, null=True, help_text="In meters")
    floor_area = models.FloatField(blank=True, null=True, help_text="In sq.m")
    total_floor_area = models.FloatField(blank=True, null=True, help_text="In sq.m")
    beams = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    columns = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    flooring = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    exterior_walls = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    corridor_walls = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    room_partitions = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    main_stair = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    window = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    ceiling = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    main_door = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    trusses = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    roof = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Fire Rating: 0 to 5")
    entry_road_width = models.PositiveSmallIntegerField(blank=True, null=True, help_text="Width in meters")

    # === State ===
    status = models.PositiveSmallIntegerField(choices=BUILDING_STATUS_CHOICES, blank=False, null=False, default=1)
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
    objects = BuildingManager()

    analytics_features = [
        'date_of_construction',
        'floor_number',
        'height',
        'floor_area',
        'total_floor_area',
        'beams',
        'columns',
        'flooring',
        'exterior_walls',
        'corridor_walls',
        'room_partitions',
        'main_stair',
        'window',
        'ceiling',
        'main_door',
        'trusses',
        'roof',
    ]

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
    def avg_fire_rating(self):
        fields = (
            'beams',
            'columns',
            'flooring',
            'exterior_walls',
            'corridor_walls',
            'room_partitions',
            'main_stair',
            'window',
            'ceiling',
            'main_door',
            'trusses',
            'roof'
        )
        total = 0
        for f in fields:
            rating = getattr(self, f)
            total += rating

        return total / len(fields)

    def age_risk(self, day):
        age = (day - self.date_of_construction).days
        chance = 0
        if age > 365:
            chance = (age / 365) * .005
        return chance

    def latest_checklist(self):
        return self.building_checklist.first()

    def is_safe(self):
        today = date.today()
        building_age = today.year - self.date_of_construction.year - (
                (today.month, today.day) < (self.date_of_construction.month, self.date_of_construction.day))
        checklist = self.latest_checklist()

        if checklist:
            result = dt_model.eval_tree(floor_number=self.floor_number, height=self.height, floor_area=self.floor_area,
                                        total_floor_area=self.total_floor_area, beams=self.beams, columns=self.columns,
                                        flooring=self.flooring, exterior_walls=self.exterior_walls,
                                        corridor_walls=self.corridor_walls, room_partitions=self.room_partitions,
                                        main_stair=self.main_stair, window=self.window, ceiling=self.ceiling,
                                        main_door=self.main_door, trusses=self.trusses, roof=self.roof,
                                        boiler_provided=checklist.boiler_provided,
                                        lpg_installation_with_permit=checklist.lpg_installation_with_permit,
                                        fuel_with_storage_permit=checklist.fuel_with_storage_permit,
                                        generator_set=checklist.generator_set,
                                        generator_fuel_storage_permit=checklist.generator_fuel_storage_permit,
                                        refuse_handling=checklist.refuse_handling,
                                        refuse_handling_fire_protection=checklist.refuse_handling_fire_protection,
                                        electrical_hazard=checklist.electrical_hazard,
                                        mechanical_hazard=checklist.mechanical_hazard,
                                        hazardous_material=checklist.hazardous_material,
                                        hazardous_material_stored=checklist.hazardous_material_stored,
                                        defects=checklist.defects,
                                        avg_fire_rating=self.avg_fire_rating(), building_age=building_age)

            if result:
                self.status = 2
                self.save()
            else:
                self.status = 0
                self.save()

            return result


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=Building)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=Building)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass
