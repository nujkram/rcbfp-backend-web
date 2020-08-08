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
    fsic_fee = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    fire_drill_certificate = models.BooleanField(default=False)
    violation_control_no = models.CharField(max_length=24, blank=True, null=True)
    electrical_inspection_no = models.CharField(max_length=24, blank=True, null=True)

    # features
    sectional_occupancy = models.PositiveSmallIntegerField(blank=True, null=True)
    occupant_load = models.PositiveSmallIntegerField(blank=True, null=True)
    egress_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
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
    main_stair_width = models.PositiveSmallIntegerField(blank=True, null=True)
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
    fire_escape_width = models.PositiveSmallIntegerField(blank=True, null=True)
    fire_escape_construction = models.CharField(max_length=254, blank=True, null=True)
    fire_escape_railings = models.BooleanField(default=False)
    fire_escape_built = models.CharField(max_length=254, blank=True, null=True)
    fire_escape_location = models.CharField(choices=LOCATION_CHOICES, blank=True, null=True, max_length=64)
    fire_escape_obstruction = models.BooleanField(default=False)
    discharge_of_exits = models.BooleanField(default=False)  # not_sure
    fire_escape_any_enclosure_provided = models.BooleanField(default=False)
    fire_escape_enclosure = models.BooleanField(default=False)
    fire_escape_opening = models.BooleanField(default=False)
    fire_escape_opening_protected = models.BooleanField(default=False)
    fire_door_provided = models.BooleanField(default=False)
    fire_door_width = models.PositiveSmallIntegerField(blank=True, null=True)
    fire_door_construction = models.CharField(max_length=254, blank=True, null=True)
    fire_door_door_proper_rating = models.BooleanField(default=False)
    fire_door_door_provided_with_vision_panel = models.BooleanField(default=False)
    fire_door_door_vision_panel_built = models.CharField(max_length=254, blank=True, null=True)
    fire_door_pressurized_stairway = models.BooleanField(default=False)
    fire_door_type_of_pressurized_stairway = models.CharField(max_length=254, blank=True, null=True)
    horizontal_exit_width = models.PositiveSmallIntegerField(blank=True, null=True)
    horizontal_exit_construction = models.CharField(max_length=254, blank=True, null=True)
    horizontal_exit_vision_panel = models.BooleanField(default=False)
    horizontal_exit_door_swing_in_direction_of_egress = models.BooleanField(default=False)
    horizontal_exit_with_self_closing_device = models.BooleanField(default=False)
    horizontal_exit_corridor_width = models.PositiveSmallIntegerField(blank=True, null=True)
    horizontal_exit_corridor_construction = models.CharField(max_length=254, blank=True, null=True)
    horizontal_exit_corridor_walls_extended = models.BooleanField(default=False)
    horizontal_exit_properly_illuminated = models.BooleanField(default=False)
    horizontal_exit_readily_visible = models.BooleanField(default=False)
    horizontal_exit_properly_marked = models.BooleanField(default=False)
    horizontal_exit_with_illuminated_directional_sign = models.BooleanField(default=False)
    horizontal_exit_properly_located = models.BooleanField(default=False)
    ramps_provided = models.BooleanField(default=False)
    ramps_type = models.CharField(choices=LOCATION_CHOICES, blank=True, null=True, max_length=64)
    ramps_width = models.PositiveSmallIntegerField(blank=True, null=True)
    ramps_class = models.CharField(max_length=254, blank=True, null=True)
    ramps_railing_provided = models.BooleanField(default=False)
    ramps_height = models.PositiveSmallIntegerField(blank=True, null=True)
    ramps_enclosure = models.BooleanField(default=False)
    ramps_construction = models.CharField(max_length=254, blank=True, null=True)
    ramps_fire_doors = models.BooleanField(default=False)
    ramps_fire_doors_width = models.PositiveSmallIntegerField(blank=True, null=True)
    ramps_fire_doors_construction = models.CharField(max_length=254, blank=True, null=True)
    ramps_with_self_closing_device = models.BooleanField(default=False)
    ramps_door_with_proper_rating = models.BooleanField(default=False)
    ramps_door_with_vision_panel = models.BooleanField(default=False)
    ramps_door_vision_panel_built = models.CharField(max_length=254, blank=True, null=True)
    ramps_door_swing_in_direction_of_egress = models.BooleanField(default=False)
    ramps_obstruction = models.BooleanField(default=False)
    ramps_discharge_of_exit = models.BooleanField(default=False)
    safe_refuge_provided = models.BooleanField(default=False)
    safe_refuge_type = models.CharField(choices=LOCATION_CHOICES, blank=True, null=True, max_length=64)
    safe_refuge_enclosure = models.BooleanField(default=False)
    safe_refuge_construction = models.CharField(max_length=254, blank=True, null=True)
    safe_refuge_fire_door = models.BooleanField(default=False)
    safe_refuge_fire_door_width = models.PositiveSmallIntegerField(blank=True, null=True)
    safe_refuge_fire_door_construction = models.CharField(max_length=254, blank=True, null=True)
    safe_refuge_with_self_closing_device = models.BooleanField(default=False)
    safe_refuge_door_proper_rating = models.BooleanField(default=False)
    safe_refuge_with_vision_panel = models.BooleanField(default=False)
    safe_refuge_vision_panel_built = models.BooleanField(default=False)
    safe_refuge_swing_in_direction_of_egress = models.BooleanField(default=False)
    emergency_light = models.BooleanField(default=False)
    emergency_light_source = models.CharField(choices=CURRENT_CHOICES, blank=True, null=True, max_length=64)
    emergency_light_per_floor_count = models.PositiveSmallIntegerField(blank=True, null=True)
    emergency_light_hallway_count = models.PositiveSmallIntegerField(blank=True, null=True)
    emergency_light_stairway_count = models.PositiveSmallIntegerField(blank=True, null=True)
    emergency_light_operational = models.BooleanField(default=False)
    emergency_light_exit_path_properly_illuminated = models.BooleanField(default=False)
    emergency_light_tested_monthly = models.BooleanField(default=False)
    exit_signs_illuminated = models.BooleanField(default=False)
    exit_signs_location = models.CharField(max_length=254, blank=True, null=True)
    exit_signs_source = models.CharField(choices=CURRENT_CHOICES, blank=True, null=True, max_length=64)
    exit_signs_visible = models.BooleanField(default=False)
    exit_signs_min_letter_size = models.PositiveSmallIntegerField(blank=True, null=True)
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
    standpipe_type = models.CharField(choices=STANDPIPE_CHOICES, blank=True, null=True, max_length=64)
    standpipe_tank_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    standpipe_location = models.CharField(max_length=254, blank=True, null=True)
    siamese_intake_provided = models.BooleanField(default=False)
    siamese_intake_location = models.CharField(max_length=254, blank=True, null=True)
    siamese_intake_size = models.PositiveSmallIntegerField(blank=True, null=True)
    siamese_intake_count = models.PositiveSmallIntegerField(blank=True, null=True)
    siamese_intake_accessible = models.BooleanField(default=False)
    fire_hose_cabinet = models.BooleanField(default=False)
    fire_hose_cabinet_accessories = models.BooleanField(default=False)
    fire_hose_cabinet_location = models.CharField(max_length=254, blank=True, null=True)
    fire_hose_per_floor_count = models.PositiveSmallIntegerField(blank=True, null=True)
    fire_hose_size = models.PositiveSmallIntegerField(blank=True, null=True)
    fire_hose_length = models.PositiveSmallIntegerField(blank=True, null=True)
    fire_hose_nozzle = models.CharField(max_length=254, blank=True, null=True)  # not_user
    fire_lane = models.BooleanField(default=False)
    fire_hydrant_location = models.CharField(max_length=254, blank=True, null=True)
    portable_fire_extinguisher_type = models.CharField(max_length=254, blank=True, null=True)  # not_sure
    portable_fire_extinguisher_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    portable_fire_extinguisher_count = models.PositiveSmallIntegerField(blank=True, null=True)
    portable_fire_extinguisher_with_ps_mark = models.BooleanField(default=False)
    portable_fire_extinguisher_with_iso_mark = models.BooleanField(default=False)
    portable_fire_extinguisher_maintained = models.BooleanField(default=False)
    portable_fire_extinguisher_conspicuously_located = models.CharField(max_length=254, blank=True, null=True)
    portable_fire_extinguisher_accessible = models.BooleanField(default=False)
    portable_fire_extinguisher_other_type = models.CharField(max_length=254, blank=True, null=True)  # not_sure
    sprinkler_system_agent_used = models.BooleanField(default=False)
    jockey_pump_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    fire_pump_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    gpm_tank_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    maintaining_line_pressure = models.BooleanField(default=False)  # not_sure
    farthest_sprinkler_head_pressure = models.CharField(max_length=254, blank=True, null=True)
    riser_size = models.PositiveSmallIntegerField(blank=True, null=True)
    type_of_heads_installed = models.CharField(max_length=254, blank=True, null=True)
    heads_per_floor_count = models.PositiveSmallIntegerField(blank=True, null=True)
    heads_total_count = models.PositiveSmallIntegerField(default=10)
    spacing_of_heads = models.CharField(max_length=254, blank=True, null=True)
    location_of_fire_dept_connection = models.CharField(max_length=254, blank=True, null=True)
    plan_submitted = models.BooleanField(default=False)
    firewall_required = models.BooleanField(default=False)
    firewall_provided = models.BooleanField(default=False)
    firewall_opening = models.BooleanField(default=False)
    boiler_provided = models.BooleanField(default=False)
    boiler_unit_count = models.PositiveSmallIntegerField(blank=True, null=True)
    boiler_fuel = models.CharField(choices=FUEL_CHOICES, blank=True, null=True, max_length=64)
    boiler_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    boiler_container = models.CharField(choices=CONTAINER_LOCATION_CHOICES, blank=True, null=True, max_length=64)
    boiler_location = models.CharField(max_length=254, blank=True, null=True)
    lpg_installation_with_permit = models.BooleanField(default=False)
    fuel_with_storage_permit = models.BooleanField(default=False)
    generator_set = models.BooleanField(default=False)
    generator_set_type = models.CharField(choices=GENERATOR_TYPE_CHOICES, blank=True, null=True, max_length=64)
    generator_fuel = models.CharField(choices=GENERATOR_FUEL_CHOICES, blank=True, null=True, max_length=64)
    generator_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    generator_location = models.CharField(max_length=254, blank=True, null=True)
    generator_bound_on_wall = models.BooleanField(default=False)
    generator_container = models.CharField(choices=CONTAINER_LOCATION_CHOICES, blank=True, null=True, max_length=64)
    generator_dispensing_system = models.CharField(choices=GENERATOR_DISPENSING_CHOICES, blank=True, null=True,
                                                   max_length=64)
    generator_output_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    generator_mechanical_permit = models.BooleanField(default=False)
    generator_fuel_storage_permit = models.BooleanField(default=False)
    generator_others = models.CharField(max_length=254, blank=True, null=True)
    generator_automatic_transfer_switch = models.BooleanField(default=False)
    generator_time_interval = models.TimeField(verbose_name='Generator time interval', blank=True, null=True)
    refuse_handling = models.BooleanField(default=False)
    refuse_handling_enclosure = models.BooleanField(default=False)
    refuse_handling_fire_resistive = models.BooleanField(default=False)
    refuse_handling_fire_protection = models.BooleanField(default=False)
    refuse_handling_fire_protection_type = models.CharField(max_length=254, blank=True, null=True)
    refuse_handling_disposal = models.BooleanField(default=False)
    refuse_handling_collection_method = models.CharField(max_length=254, blank=True, null=True)
    electrical_hazard = models.BooleanField(default=False)
    electrical_hazard_location = models.CharField(max_length=254, blank=True, null=True)
    mechanical_hazard = models.BooleanField(default=False)
    mechanical_hazard_location = models.CharField(max_length=254, blank=True, null=True)
    elevator_count = models.PositiveSmallIntegerField(blank=True, null=True)
    fireman_elevator = models.BooleanField(default=False)
    fireman_elevator_key = models.BooleanField(default=False)
    other_service_system = models.CharField(choices=SERVICE_SYSTEM_CHOICES, blank=True, null=True, max_length=64)
    hazardous_area = models.CharField(choices=HAZARDOUS_AREA_CHOICES, blank=True, null=True, max_length=64)
    hazardous_area_other = models.CharField(max_length=254, blank=True, null=True)
    separation_fire_rated = models.BooleanField(default=False)
    type_of_protection = models.CharField(max_length=254, blank=True, null=True)
    separation_fire_rated_count = models.PositiveSmallIntegerField(blank=True, null=True)
    separation_fire_rated_capacity = models.PositiveSmallIntegerField(blank=True, null=True)
    separation_fire_rated_accessible = models.BooleanField(default=False)
    separation_fire_rated_fuel = models.BooleanField(default=False)
    separation_fire_rated_location = models.CharField(max_length=254, blank=True, null=True)
    separation_fire_rated_permit = models.BooleanField(default=False)
    chimney_built = models.CharField(max_length=254, blank=True, null=True)
    chimney_spark_arrestor = models.BooleanField(default=False)
    chimney_smoke_hood = models.BooleanField(default=False)
    hazardous_material = models.BooleanField(default=False)
    hazardous_material_stored = models.BooleanField(default=False)
    fire_brigade_organization = models.BooleanField(default=False)
    fire_safety_seminar = models.BooleanField(default=False)
    employee_trained_in_emergency_procedures = models.BooleanField(default=False)
    evacuation_drill_first = models.BooleanField(default=False)
    evacuation_drill_second = models.BooleanField(default=False)
    defects = models.PositiveSmallIntegerField(default=0)
    defects_photo = models.FileField(verbose_name='Defects supporting image', upload_to=defect_upload_path,
                                     max_length=254,
                                     blank=True, null=True)
    recommendations = models.CharField(max_length=254, blank=True, null=True)

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
        related_name='main_stair_pressurized_stairway_datetime'
    )
    fire_door_pressurized_stairway_last_tested = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='fire_door_pressurized_stairway_datetime'
    )
    vertical_opening_last_tested = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='vertical_opening_datetime'
    )
    fire_hose_last_tested = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='fire_hose_datetime'
    )
    sprinkler_system_last_tested = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='sprinkler_system_datetime'
    )
    sprinkler_system_last_conducted = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='sprinkler_system_conducted_datetime'
    )
    certificate_of_installation_date = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='certificate_of_installation_datetime'
    )
    generator_mechanical_permit_date_issued = models.ForeignKey(
        'datesdim.DateDim',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='generator_permit_datetime'
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
    objects = ChecklistManager()

    analytics_features = [
        'boiler_provided',
        'boiler_container',
        'lpg_installation_with_permit',
        'fuel_with_storage_permit',
        'generator_set',
        'generator_fuel_storage_permit',
        'refuse_handling',
        'refuse_handling_fire_protection',
        'electrical_hazard',
        'mechanical_hazard',
        'hazardous_material',
        'hazardous_material_stored',
        'defects',
    ]

    class Meta:
        ordering = ('building',)
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
    def count_score(self):
        score = 0
        fields = []

        for field in Checklist._meta.fields:
            if isinstance(field, BooleanField):
                if field.name not in EXCLUDE_FIELDS:
                    fields.append(field.name)
                    score += getattr(self, field.name)

        return score

    def get_score(self):
        """
        factors
        - kitid nga dalan
        - checklist
        """
        score = self.count_score()

        return score

    def fire_rating(self):
        score_percentage = self.get_score() / 129 * 100

        return score_percentage

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

        if self.refuse_handling and (not self.refuse_handling_fire_protection or self.refuse_handling_fire_resistive):
            chance_of_fire += 0.02

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
