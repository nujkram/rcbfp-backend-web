"""
rcbfp Module
---
checklists - Checklist Master Model 0.0.1
This is the Master model for Checklist
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
from buildings.constants import LOCATION_CHOICES, CURRENT_CHOICES, STANDPIPE_CHOICES
from checklists.models.checklist.managers.checklist_managers import ChecklistManager


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
  building_permit = models.BooleanField(default=False)
  occupancy_permit = models.BooleanField(default=False)
  fsic_control_no = models.CharField(max_length=18, blank=True, null=True)
  fsic_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
  fire_drill_certificate = models.BooleanField(default=False)
  violation_control_no = models.CharField(max_length=24, blank=True, null=True)
  electrical_inspection_no = models.CharField(max_length=24, blank=True, null=True)
  sectional_occupancy = models.PositiveSmallIntegerField(blank=True, null=True)
  occupant_load = models.PositiveSmallIntegerField(blank=True, null=True)
  egress_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
  first_name = models.CharField(max_length=24, blank=True, null=True)
  middle_name = models.CharField(max_length=24, blank=True, null=True)
  last_name = models.CharField(max_length=24, blank=True, null=True)
  policy_no = models.CharField(max_length=24, blank=True, null=True)
  any_renovation = models.BooleanField(default=False)
  renovation_specification = models.CharField(max_length=254, blank=True, null=True)
  horizontal_exit_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
  exit_stair_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
  no_of_exits = models.PositiveSmallIntegerField(blank=True, null=True)
  is_exits_remote = models.BooleanField(default=False)
  exit_location = models.CharField(max_length=254, blank=True, null=True)
  any_enclosure = models.BooleanField(default=False)
  is_exit_accessible = models.BooleanField(default=False)
  is_fire_doors_provided = models.BooleanField(default=False)
  self_closing_mechanism = models.BooleanField(default=False)
  panic_hardware = models.BooleanField(default=False)
  readily_accessible = models.BooleanField(default=False)
  travel_distance_within_limit = models.BooleanField(default=False)
  adequate_illumination = models.BooleanField(default=False)
  panic_hardware_operational = models.BooleanField(default=False)
  doors_open_easily = models.BooleanField(default=False)
  bldg_with_mezzanine = models.BooleanField(default=False)
  is_obstructed = models.BooleanField(default=False)
  dead_ends_within_limits = models.BooleanField(default=False)
  proper_rating_illumination = models.BooleanField(default=False)
  door_swing_in_the_direction_of_exit = models.BooleanField(default=False)
  self_closure_operational = models.BooleanField(default=False)
  mezzanine_with_proper_exits = models.BooleanField(default=False)
  corridors_of_sufficient_size = models.BooleanField(default=False)
  main_stair_width = models.FloatField(blank=True, null=True)
  construction = models.CharField(max_length=254, blank=True, null=True)  # not_sure
  main_stair_railings = models.BooleanField(default=False)
  main_stair_railings_built = models.CharField(max_length=254, blank=True, null=True)
  main_stair_any_enclosure_provided = models.BooleanField(default=False)
  enclosure_built = models.CharField(max_length=254, blank=True, null=True)
  any_openings = models.BooleanField(default=False)
  main_stair_door_proper_rating = models.BooleanField(default=False)
  main_stair_door_provided_with_vision_panel = models.BooleanField(default=False)
  main_stair_door_vision_panel_built = models.CharField(max_length=254, blank=True, null=True)
  main_stair_pressurized_stairway = models.BooleanField(default=False)
  main_stair_type_of_pressurized_stairway = models.CharField(max_length=254, blank=True, null=True)
  fire_escape_count = models.PositiveSmallIntegerField(blank=True, null=True)
  fire_escape_width = models.FloatField(blank=True, null=True)
  fire_escape_construction = models.CharField(max_length=254, blank=True, null=True)
  fire_escape_railings = models.BooleanField(default=False)
  fire_escape_built = models.CharField(max_length=254, blank=True, null=True)
  location = models.CharField(choices=LOCATION_CHOICES, default='Interior')
  fire_escape_obstruction = models.BooleanField(default=False)
  discharge_of_exits = models.BooleanField(default=False)  # not_sure
  fire_escape_any_enclosure_provided = models.BooleanField(default=False)
  fire_escape_enclosure = models.BooleanField(default=False)
  fire_escape_opening = models.BooleanField(default=False)
  fire_escape_opening_protected = models.BooleanField(default=False)
  fire_door_provided = models.BooleanField(default=False)
  fire_door_width = models.FloatField(blank=True, null=True)
  fire_door_construction = models.CharField(max_length=254, blank=True, null=True)
  fire_door_door_proper_rating = models.BooleanField(default=False)
  fire_door_door_provided_with_vision_panel = models.BooleanField(default=False)
  fire_door_door_vision_panel_built = models.CharField(max_length=254, blank=True, null=True)
  fire_door_pressurized_stairway = models.BooleanField(default=False)
  fire_door_type_of_pressurized_stairway = models.CharField(max_length=254, blank=True, null=True)
  horizontal_exit_width = models.FloatField(blank=True, null=True)
  horizontal_exit_construction = models.CharField(max_length=254, blank=True, null=True)
  horizontal_exit_vision_panel = models.BooleanField(default=False)
  horizontal_exit_door_swing_in_direction_of_egress = models.BooleanField(default=False)
  horizontal_exit_with_self_closing_device = models.BooleanField(default=False)
  horizontal_exit_corridor_width = models.FloatField(blank=True, null=True)
  horizontal_exit_corridor_construction = models.CharField(max_length=254, blank=True, null=True)
  horizontal_exit_corridor_walls_extended = models.BooleanField(default=False)
  horizontal_exit_properly_illuminated = models.BooleanField(default=False)
  horizontal_exit_readily_visible = models.BooleanField(default=False)
  horizontal_exit_properly_marked = models.BooleanField(default=False)
  horizontal_exit_with_illuminated_directional_sign = models.BooleanField(default=False)
  horizontal_exit_properly_located = models.BooleanField(default=False)
  ramps_provided = models.BooleanField(default=False)
  ramps_type = models.CharField(choices=LOCATION_CHOICES, default='Interior')
  ramps_width = models.FloatField(blank=True, null=True)
  ramps_class = models.CharField(max_length=254, blank=True, null=True)
  ramps_railing_provided = models.BooleanField(default=False)
  ramps_height = models.FloatField(blank=True, null=True)
  ramps_enclosure = models.BooleanField(default=False)
  ramps_construction = models.CharField(max_length=254, blank=True, null=True)
  ramps_fire_doors = models.BooleanField(default=False)
  ramps_fire_doors_width = models.FloatField(blank=True, null=True)
  ramps_fire_doors_construction = models.CharField(max_length=254, blank=True, null=True)
  ramps_with_self_closing_device = models.BooleanField(default=False)
  ramps_door_with_proper_rating = models.BooleanField(default=False)
  ramps_door_with_vision_panel = models.BooleanField(default=False)
  ramps_door_vision_panel_built = models.CharField(max_length=254, blank=True, null=True)
  ramps_door_swing_in_direction_of_egress = models.BooleanField(default=False)
  ramps_obstruction = models.BooleanField(default=False)
  ramps_discharge_of_exit = models.BooleanField(default=False)
  safe_refuge_provided = models.BooleanField(default=False)
  safe_refuge_type = models.CharField(choices=LOCATION_CHOICES, default='Interior')
  safe_refuge_enclosure = models.BooleanField(default=False)
  safe_refuge_construction = models.CharField(max_length=254, blank=True, null=True)
  safe_refuge_fire_door = models.BooleanField(default=False)
  safe_refuge_fire_door_width = models.FloatField(blank=True, null=True)
  safe_refuge_fire_door_construction = models.CharField(max_length=254, blank=True, null=True)
  safe_refuge_with_self_closing_device = models.BooleanField(default=False)
  safe_refuge_door_proper_rating = models.BooleanField(default=False)
  safe_refuge_with_vision_panel = models.BooleanField(default=False)
  safe_refuge_vision_panel_built = models.BooleanField(default=False)
  safe_refuge_swing_in_direction_of_egress = models.BooleanField(default=False)
  emergency_light = models.BooleanField(default=False)
  emergency_light_source = models.CharField(choices=CURRENT_CHOICES, default='AC/DC')
  emergency_light_per_floor_count = models.PositiveSmallIntegerField(blank=True, null=True)
  emergency_light_hallway_count = models.PositiveSmallIntegerField(blank=True, null=True)
  emergency_light_stairway_count = models.PositiveSmallIntegerField(blank=True, null=True)
  emergency_light_operational = models.BooleanField(default=False)
  emergency_light_exit_path_properly_illuminated = models.BooleanField(default=False)
  emergency_light_tested_monthly = models.BooleanField(default=False)
  exit_signs_illuminated = models.BooleanField(default=False)
  exit_signs_location = models.CharField(max_length=254, blank=True, null=True)
  exit_signs_source = models.CharField(choices=CURRENT_CHOICES, default='AC/DC')
  exit_signs_visible = models.BooleanField(default=False)
  exit_signs_min_letter_size = models.FloatField(blank=True, null=True)
  exit_route_posted_on_lobby = models.BooleanField(default=False)
  exit_route_posted_on_rooms = models.BooleanField(default=False)
  directional_exit_signs = models.BooleanField(default=False)
  directional_exit_signs_location = models.CharField(max_length=254, blank=True, null=True)
  no_smoking_sign = models.BooleanField(default=False)
  dead_end_sign = models.BooleanField(default=False)
  elevator_sign = models.BooleanField(default=False)
  keep_door_closed_sign = models.BooleanField(default=False)
  others = models.CharField(max_length=254, blank=True, null=True)
  vertical_openings_properly_protected = models.BooleanField(default=False)
  vertical_openings_atrium = models.BooleanField(default=False)
  fire_doors_good_condition = models.BooleanField(default=False)
  elevator_opening_protected = models.BooleanField(default=False)
  pipe_chase_opening_protected = models.BooleanField(default=False)
  aircon_ducts_with_dumper = models.BooleanField(default=False)
  garbage_chute_protected = models.BooleanField(default=False)
  between_floor_protected = models.BooleanField(default=False)
  standpipe_type = models.CharField(choices=STANDPIPE_CHOICES, default='Dry')
  standpipe_tank_capacity = models.FloatField(blank=True, null=True)
  standpipe_location = models.CharField(max_length=254, blank=True, null=True)
  siamese_intake_provided = models.BooleanField(default=False)
  siamese_intake_location = models.CharField(max_length=254, blank=True, null=True)
  siamese_intake_size = models.FloatField(blank=True, null=True)
  siamese_intake_count = models.PositiveSmallIntegerField(blank=True, null=True)
  siamese_intake_accessible = models.BooleanField(default=False)
  fire_hose_cabinet = models.BooleanField(default=False)
  fire_hose_cabinet_accessories = models.BooleanField(default=False)
  fire_hose_cabinet_location = models.CharField(max_length=254, blank=True, null=True)
  fire_hose_per_floor_count = models.PositiveSmallIntegerField(blank=True, null=True)
  fire_hose_size = models.FloatField(blank=True, null=True)
  fire_hose_length = models.FloatField(blank=True, null=True)
  fire_hose_nozzle = models.CharField(max_length=254, blank=True, null=True)  # not_user
  fire_lane = models.BooleanField(default=False)
  fire_hydrant_location = models.CharField(max_length=254, blank=True, null=True)
  portable_fire_extinguisher_type = models.CharField(max_length=254, blank=True, null=True)  # not_sure
  portable_fire_extinguisher_capacity = models.FloatField(blank=True, null=True)
  portable_fire_extinguisher_count = models.PositiveSmallIntegerField(blank=True, null=True)
  portable_fire_extinguisher_with_ps_mark = models.BooleanField(default=False)
  portable_fire_extinguisher_with_iso_mark = models.BooleanField(default=False)
  portable_fire_extinguisher_maintained = models.BooleanField(default=False)
  portable_fire_extinguisher_conspicuously_located = models.CharField(max_length=254, blank=True, null=True)
  portable_fire_extinguisher_accessible = models.BooleanField(default=False)
  portable_fire_extinguisher_other_type = models.CharField(max_length=254, blank=True, null=True)  # not_sure
  sprinkler_system_agent_used = models.BooleanField(default=False)
  jockey_pump_capacity = models.FloatField(blank=True, null=True)
  fire_pump_capacity = models.FloatField(blank=True, null=True)
  gpm_tank_capacity = models.FloatField(blank=True, null=True)
  maintaining_line_pressure = models.BooleanField(default=False)  # not_sure
  farthest_sprinkler_head_pressure = models.CharField(max_length=254, blank=True, null=True)
  riser_size = models.FloatField(blank=True, null=True)
  type_of_heads_installed = models.CharField(max_length=254, blank=True, null=True)
  heads_per_floor_count = models.PositiveSmallIntegerField(blank=True, null=True)
  heads_total_count = models.PositiveSmallIntegerField(blank=True, null=True)
  spacing_of_heads = models.CharField(max_length=254, blank=True, null=True)
  location_of_fire_dept_connection = models.CharField(max_length=254, blank=True, null=True)
  plan_submitted = models.BooleanField(default=False)
  firewall_required = models.BooleanField(default=False)
  firewall_provided = models.BooleanField(default=False)
  firewall_opening = models.BooleanField(default=False)
  boiler_provided = models.BooleanField(default=False)
  boiler_unit_count = models.PositiveSmallIntegerField(blank=True, null=True)

  # === State ===
  active = models.BooleanField(default=True)
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
  building_permit_date_issued = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='building_issued_datetime'
  )
  occupancy_permit_date_issued = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='occupancy_issued_datetime'
  )
  fsic_date_issued = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='fsic_issued_datetime'
  )
  fire_drill_certificate_date_issued = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='fire_drill_datetime'
  )
  violation_control_no_date_issued = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='violation_control_no_datetime'
  )
  electrical_inspection_date_issued = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='electrical_inspection_datetime'
  )
  insurance_date_issued = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  main_stair_pressurized_stairway_last_tested = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  fire_door_pressurized_stairway_last_tested = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  vertical_opening_last_tested = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  fire_hose_last_tested = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  sprinkler_system_last_tested = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  sprinkler_system_last_conducted = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  certificate_of_installation_date = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.SET_NULL,
    related_name='issurance_datetime'
  )
  date_checked = models.ForeignKey(
    'datesdim.DateDim',
    blank=True,
    null=True,
    on_delete=models.CASCADE,
    related_name='checked_datetime'
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
  objects = ChecklistManager

  class Meta:
    ordering = ('name',)
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


################################################################################
# === Signals ===
################################################################################
@receiver(post_save, sender=Checklist)
def scaffold_post_save(sender, instance=None, created=False, **kwargs):
  pass


@receiver(pre_save, sender=Checklist)
def scaffold_pre_save(sender, instance=None, created=False, **kwargs):
  pass
