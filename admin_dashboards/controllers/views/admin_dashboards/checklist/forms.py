from django import forms

from buildings.models.building.building_models import Building
from business.models import Business


class ChecklistForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    policy_no = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    building_permit = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    occupancy_permit = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fsic_control_no = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fsic_fee = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_drill_certificate = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    violation_control_no = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    electrical_inspection_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sectional_occupancy = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    occupant_load = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    egress_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    any_renovation = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    renovation_specification = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_stair_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_of_exits = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_exits_remote = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    any_enclosure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_exit_accessible = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_fire_doors_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    self_closing_mechanism = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    panic_hardware = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    readily_accessible = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    travel_distance_within_limit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    adequate_illumination = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    panic_hardware_operational = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    doors_open_easily = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bldg_with_mezzanine = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_obstructed = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dead_ends_within_limits = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    proper_rating_illumination = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    door_swing_in_the_direction_of_exit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    self_closure_operational = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mezzanine_with_proper_exits = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    corridors_of_sufficient_size = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_railings = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_railings_built = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_any_enclosure_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    enclosure_built = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    any_openings = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_door_proper_rating = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_door_provided_with_vision_panel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_door_vision_panel_built = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_pressurized_stairway = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    main_stair_type_of_pressurized_stairway = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_railings = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_built = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_obstruction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    discharge_of_exits = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_any_enclosure_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_enclosure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_opening = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_escape_opening_protected = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_door_proper_rating = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_door_provided_with_vision_panel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_door_vision_panel_built = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_pressurized_stairway = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_door_type_of_pressurized_stairway = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_vision_panel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_door_swing_in_direction_of_egress = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_with_self_closing_device = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_corridor_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_corridor_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_corridor_walls_extended = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_properly_illuminated = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_readily_visible = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_properly_marked = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_with_illuminated_directional_sign = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    horizontal_exit_properly_located = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_class = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_railing_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_height = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_enclosure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_fire_doors = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_fire_doors_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_fire_doors_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_with_self_closing_device = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_door_with_proper_rating = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_door_with_vision_panel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_door_vision_panel_built = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_door_swing_in_direction_of_egress = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_obstruction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    ramps_discharge_of_exit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_enclosure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_fire_door = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_fire_door_width = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_fire_door_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_with_self_closing_device = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_door_proper_rating = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_with_vision_panel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_vision_panel_built = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safe_refuge_swing_in_direction_of_egress = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light_source = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light_per_floor_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light_hallway_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light_stairway_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light_operational = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light_exit_path_properly_illuminated = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    emergency_light_tested_monthly = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_signs_illuminated = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_signs_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_signs_source = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_signs_visible = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_signs_min_letter_size = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_route_posted_on_lobby = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_route_posted_on_rooms = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    directional_exit_signs = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    directional_exit_signs_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_smoking_sign = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    dead_end_sign = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    elevator_sign = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    keep_door_closed_sign = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    vertical_openings_properly_protected = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    vertical_openings_atrium = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_doors_good_condition = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    elevator_opening_protected = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pipe_chase_opening_protected = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    aircon_ducts_with_dumper = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    garbage_chute_protected = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    between_floor_protected = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    standpipe_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    standpipe_tank_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    standpipe_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    siamese_intake_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    siamese_intake_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    siamese_intake_size = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    siamese_intake_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    siamese_intake_accessible = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hose_cabinet = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hose_cabinet_accessories = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hose_cabinet_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hose_per_floor_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hose_size = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hose_length = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hose_nozzle = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_lane = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_hydrant_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_with_ps_mark = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_with_iso_mark = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_maintained = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_conspicuously_located = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_accessible = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    portable_fire_extinguisher_other_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sprinkler_system_agent_used = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    jockey_pump_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_pump_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    gpm_tank_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    maintaining_line_pressure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    farthest_sprinkler_head_pressure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    riser_size = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type_of_heads_installed = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    heads_per_floor_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    heads_total_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    spacing_of_heads = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    location_of_fire_dept_connection = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    plan_submitted = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    firewall_required = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    firewall_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    firewall_opening = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    boiler_provided = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    boiler_unit_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    boiler_fuel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    boiler_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    boiler_container = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    boiler_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    lpg_installation_with_permit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fuel_with_storage_permit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_set = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_set_type = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_fuel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_bound_on_wall = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_container = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_dispensing_system = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_output_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_mechanical_permit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_fuel_storage_permit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_others = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_automatic_transfer_switch = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    generator_time_interval = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    refuse_handling = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    refuse_handling_enclosure = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    refuse_handling_fire_protection = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    electrical_hazard = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    electrical_hazard_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mechanical_hazard = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mechanical_hazard_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    elevator_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    other_service_system = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hazardous_area = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hazardous_area_other = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    separation_fire_rated = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    type_of_protection = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    separation_fire_rated_count = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    separation_fire_rated_capacity = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    separation_fire_rated_accessible = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    separation_fire_rated_fuel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    separation_fire_rated_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    separation_fire_rated_permit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hazardous_material = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hazardous_material_stored = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_brigade_organization = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_safety_seminar = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    employee_trained_in_emergency_procedures = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    evacuation_drill_first = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    evacuation_drill_second = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    defects = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    defects_photo = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    recommendations = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    building = forms.ModelChoiceField(queryset=Building.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    business = forms.ModelChoiceField(queryset=Business.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    building_permit_date_issued = forms.DateTimeField(required=True)
    occupancy_permit_date_issued = forms.DateTimeField(required=True)
    fsic_date_issued = forms.DateTimeField(required=True)
    fire_drill_certificate_date_issued = forms.DateTimeField(required=True)
    violation_control_no_date_issued = forms.DateTimeField(required=True)
    electrical_inspection_date_issued = forms.DateTimeField(required=True)
    insurance_date_issued = forms.DateTimeField(required=True)
    main_stair_pressurized_stairway_last_tested = forms.DateTimeField(required=True)
    fire_door_pressurized_stairway_last_tested = forms.DateTimeField(required=True)
    vertical_opening_last_tested = forms.DateTimeField(required=True)
    fire_hose_last_tested = forms.DateTimeField(required=True)
    sprinkler_system_last_tested = forms.DateTimeField(required=True)
    sprinkler_system_last_conducted = forms.DateTimeField(required=True)
    certificate_of_installation_date = forms.DateTimeField(required=True)
    generator_mechanical_permit_date_issued = forms.DateTimeField(required=True)
    date_checked = forms.DateTimeField(required=True)