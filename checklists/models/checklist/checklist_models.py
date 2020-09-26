"""
rcbfp Module
---
checklists - Checklist Master Model 0.0.1
This is the Master model for Checklist
---
Author: Mark Gersaniva
Email: mark.gersaniva@springvalley.tech
"""
import uuid

from django.contrib.postgres.forms import JSONField
from django.db import models
from django.apps import apps
from django.db.models import BooleanField
from django.dispatch import receiver
from django_extensions.db import fields as extension_fields
from django.db.models.signals import post_save, pre_save

# Model manager
from buildings.constants import LOCATION_CHOICES, CURRENT_CHOICES, STANDPIPE_CHOICES, FUEL_CHOICES, \
    CONTAINER_LOCATION_CHOICES, GENERATOR_TYPE_CHOICES, GENERATOR_FUEL_CHOICES, GENERATOR_DISPENSING_CHOICES, \
    SERVICE_SYSTEM_CHOICES, HAZARDOUS_AREA_CHOICES
from checklists.constants import REMARKS_CHOICES, STATUS_CHOICES
from checklists.models.checklist.managers.checklist_managers import ChecklistManager

EXCLUDE_FIELDS = ['active']


def defect_upload_path(intance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4}.{ext}'
    return f'upload/defects/{filename}'


class Checklist(models.Model):
    """
    The Checklist class defines the master data model for Checklist
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
    first_name = models.CharField(max_length=24, blank=True, null=True)
    middle_name = models.CharField(max_length=24, blank=True, null=True)
    last_name = models.CharField(max_length=24, blank=True, null=True)
    policy_no = models.CharField(max_length=24, blank=True, null=True)
    building_permit = models.BooleanField(default=False)
    occupancy_permit = models.BooleanField(default=False)
    fsic_control_no = models.CharField(max_length=18, blank=True, null=True)
    fsic_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True, default=0)
    fire_drill_certificate = models.BooleanField(default=False)
    violation_control_no = models.CharField(max_length=24, blank=True, null=True)
    electrical_inspection_no = models.CharField(max_length=24, blank=True, null=True)
    sectional_occupancy = models.CharField(max_length=1024, blank=True, null=True)

    # Means of egress
    exits_count = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    exits_width = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    exits_accessible = models.BooleanField(default=False)
    termination_of_exit = models.CharField(max_length=254, blank=True, null=True)
    exits_enclosure_provided = models.BooleanField(default=False)
    exits_enclosure_construction = models.CharField(max_length=254, blank=True, null=True)
    exits_fire_doors_provided = models.BooleanField(default=False)
    exits_fire_door_construction = models.CharField(max_length=254, blank=True, null=True)
    stairs_count = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    stairs_enclosure_provided = models.BooleanField(default=False)
    stairs_enclosure_construction = models.CharField(max_length=254, blank=True, null=True)
    stairs_fire_doors_provided = models.BooleanField(default=False)
    stairs_fire_door_construction = models.CharField(max_length=254, blank=True, null=True)
    other_details = models.CharField(max_length=1024, blank=True, null=True)

    # Emergency equipment
    emergency_light = models.BooleanField(default=False)
    exit_signs_illuminated = models.BooleanField(default=False)
    fire_extinguisher_count = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    fire_extinguisher_accessible = models.BooleanField(default=False)
    fire_extinguisher_conspicuous_location = models.BooleanField(default=False)
    fire_alarm = models.BooleanField(default=False)
    detectors = models.BooleanField(default=False)
    control_panel_location = models.CharField(max_length=254, blank=True, null=True)
    control_panel_functional = models.BooleanField(default=False)

    # Flammables
    hazardous_materials = models.BooleanField(default=False)
    hazardous_materials_properly_stored = models.BooleanField(default=False)
    no_smoking_sign = models.BooleanField(default=False)
    smoking_permitted = models.BooleanField(default=False)
    smoking_area_location = models.CharField(max_length=254, blank=True, null=True)
    storage_location = models.CharField(max_length=254, blank=True, null=True)
    safety_device_for_lpg = models.BooleanField(default=False)
    oven_used = models.CharField(max_length=254, blank=True, null=True)
    kind_of_fuel = models.CharField(max_length=254, blank=True, null=True)
    smoke_hood = models.CharField(max_length=254, blank=True, null=True)
    spark_arrester = models.CharField(max_length=254, blank=True, null=True)
    partition_construction = models.CharField(max_length=254, blank=True, null=True)

    defects = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    building_permit_date_issued = models.DateField(null=True, blank=True)
    occupancy_permit_date_issued = models.DateField(null=True, blank=True)
    fsic_date_issued = models.DateField(null=True, blank=True)
    fire_drill_certificate_date_issued = models.DateField(null=True, blank=True)
    violation_control_no_date_issued = models.DateField(null=True, blank=True)
    electrical_inspection_date_issued = models.DateField(null=True, blank=True)
    insurance_date_issued = models.DateField(null=True, blank=True)
    notes = models.CharField(max_length=1024, blank=True, null=True)
    recommendations = models.CharField(max_length=1024, blank=True, null=True)

    # === State ===
    active = models.BooleanField(default=True)
    status = models.PositiveSmallIntegerField(choices=STATUS_CHOICES, blank=True, null=True, default=0)
    remarks = models.PositiveIntegerField(choices=REMARKS_CHOICES, blank=True, null=True, default=1)
    meta = JSONField()

    # === Relationship Fields ===
    building = models.ForeignKey(
        'buildings.Building',
        on_delete=models.CASCADE,
        null=False,
        db_index=False,
        related_name='building_checklist',
        blank=False
    )
    business = models.ForeignKey(
        'business.Business',
        on_delete=models.CASCADE,
        null=True,
        db_index=False,
        related_name='business_checklists',
        blank=True
    )
    inspection = models.ForeignKey(
        'inspections.InspectionSchedule',
        on_delete=models.CASCADE,
        null=True,
        db_index=False,
        related_name='inspection_checklist',
        blank=True
    )
    date_checked = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='date_checked_checklist'
    )
    created_by = models.ForeignKey(
        'accounts.Account',
        on_delete=models.SET_NULL,
        null=True,
        db_index=False,
        related_name='created_checklists',
        blank=True
    )
    last_updated_by = models.ForeignKey(
        'accounts.Account',
        on_delete=models.SET_NULL,
        null=True,
        db_index=False,
        related_name='updated_checklists',
        blank=True
    )

    # Manager
    objects = ChecklistManager()

    analytics_features = [
        'defects',
    ]

    class Meta:
        ordering = ('date_checked',)
        verbose_name = "Checklist"
        verbose_name_plural = "Checklists"

    ################################################################################
    # === Builtin methods ===
    ################################################################################
    def __str__(self):
        return f'{self.business.name}'

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
        if self.middle_name:
            return f'{self.first_name} {self.middle_name[0]}. {self.last_name}'
        return f'{self.first_name} {self.last_name}'

    def get_boolean_fields(self):
        field_count = 0

        for field in Checklist._meta.fields:
            if isinstance(field, BooleanField):
                if field.name not in EXCLUDE_FIELDS:
                    field_count += 1

        return field_count

    def count_score(self):
        score = 0
        fields = []

        for field in Checklist._meta.fields:
            if isinstance(field, BooleanField):
                if field.name not in EXCLUDE_FIELDS:
                    fields.append(field.name)
                    score += getattr(self, field.name)

        return score

    def avg_checklist_rating(self):
        field_count = self.get_boolean_fields()

        total = self.count_score()
        if total != 0:
            avg = total / field_count

            return avg
        return 0

    def percentage_checklist_rating(self):
        field_count = self.get_boolean_fields()
        score_percentage = self.count_score() / field_count * 100

        return score_percentage

    def result(self):
        rating = self.percentage_checklist_rating()
        if rating >= 85:
            return True
        else:
            return False

    def risk(self):
        chance_of_fire = 0.001

        if self.boiler_provided:
            chance_of_fire += 0.05

        if self.boiler_container == 'Above Ground':
            chance_of_fire += 0.01

        if self.lpg_installation_with_permit:
            chance_of_fire += 0.02

        if self.fuel_with_storage_permit:
            chance_of_fire += 0.02
        else:
            chance_of_fire += 0.2

        if self.generator_set:
            chance_of_fire += 0.02

        if self.generator_fuel == 'Gasoline':
            chance_of_fire += 0.3

        if self.generator_fuel and not self.generator_fuel_storage_permit:
            chance_of_fire += 0.1

        if self.electrical_hazard:
            chance_of_fire += 0.2

        if self.mechanical_hazard:
            chance_of_fire += 0.1

        if self.hazardous_material:
            chance_of_fire += 0.15

        if self.hazardous_material_stored:
            chance_of_fire += 0.01

        if self.hazardous_area == "Kitchen":
            chance_of_fire += 0.1

        if not self.defects:
            self.defects = 0

        if 0 < self.defects <= 100:
            chance_of_fire += self.defects * 0.01

        if self.defects > 100:
            chance_of_fire += .22

        return chance_of_fire


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=Checklist)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
    pass


@receiver(pre_save, sender=Checklist)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
    pass
