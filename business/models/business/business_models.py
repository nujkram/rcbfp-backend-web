"""
rcbfp Module
---
startup_ratings - Application Master Model 0.0.1
This is the Master model for Application
---
Author: Mark Gersaniva
Email: mark.gersaniva@springvalley.tech
"""
from datetime import date

from django.contrib.postgres.forms import JSONField
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField

import dt_model
from business.constants import BUSINESS_STATUS_CHOICES, APPROVED, FAILED
from business.models.business.managers.business_managers import BusinessManager
from checklists.models.checklist.checklist_models import Checklist


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
    is_new = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    status = models.PositiveSmallIntegerField(choices=BUSINESS_STATUS_CHOICES, blank=False, null=False, default=1)
    meta = JSONField()

    # === Relationship Fields ===
    building = models.ForeignKey('buildings.Building', blank=True, null=True, on_delete=models.CASCADE,
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

    def latest_checklist(self):
        return self.business_checklists.order_by('-pk').first()

    def is_safe(self, *args, **kwargs):
        today = date.today()
        building_age = today.year - self.building.date_of_construction.year - (
                (today.month, today.day) < (
            self.building.date_of_construction.month, self.building.date_of_construction.day))
        if 'checklist_pk' in kwargs:
            checklist = Checklist.objects.get(pk=kwargs['checklist_pk'])
        else:
            checklist = self.latest_checklist()

        if checklist is not None:
            result = dt_model.eval_tree(
                beams=self.building.beams, columns=self.building.columns,
                flooring=self.building.flooring,
                exterior_walls=self.building.exterior_walls,
                corridor_walls=self.building.corridor_walls,
                room_partitions=self.building.room_partitions,
                main_stair=self.building.main_stair, window=self.building.window,
                ceiling=self.building.ceiling,
                main_door=self.building.main_door, trusses=self.building.trusses,
                roof=self.building.roof,
                defects=checklist.defects, checklist_rating=checklist.percentage_checklist_rating(),
                avg_fire_rating=self.building.avg_fire_rating(), building_age=building_age
            )
            if result:
                self.status = APPROVED
                self.save()

                if checklist.result():
                    self.status = APPROVED
                else:
                    self.status = FAILED

                self.building.status = APPROVED
                self.building.save()

                # reverse result
                # result = True
            else:
                self.status = FAILED
                self.save()

                self.building.status = FAILED
                self.building.save()

                # reverse result
                # result = False
            self.save()

            return result
        else:
            return False
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
