from django.db import models
from django.apps import apps

from datesdim.models import DateDim


class ChecklistQuerySet(models.QuerySet):
    def actives(self):
        return self.filter(active=True)


class ChecklistManager(models.Manager):
    def get_queryset(self):
        return ChecklistQuerySet(self.model, using=self._db)

    def actives(self):
        return self.get_queryset().actives()

    def create(self, *args, **kwargs):
        flag = True
        m = []
        date_value = kwargs['date_checked']
        try:
            checked_date = DateDim.objects.get(year=date_value.year, month=date_value.month, day=date_value.day)
        except DateDim.DoesNotExist:
            flag = False
            m.append(f'{checked_date} is an invalid building')

        if kwargs['policy_no']:
            policy_no = kwargs['policy_no']
        else:
            policy_no = 0

        if kwargs['building_permit']:
            building_permit = kwargs['building_permit']
        else:
            building_permit = 0

        if kwargs['occupancy_permit']:
            occupancy_permit = kwargs['occupancy_permit']
        else:
            occupancy_permit = 0

        if kwargs['fsic_control_no']:
            fsic_control_no = kwargs['fsic_control_no']
        else:
            fsic_control_no = 0

        if kwargs['fsic_fee']:
            fsic_fee = kwargs['fsic_fee']
        else:
            fsic_fee = 0

        if kwargs['fire_drill_certificate']:
            fire_drill_certificate = kwargs['fire_drill_certificate']
        else:
            fire_drill_certificate = 0

        if kwargs['violation_control_no']:
            violation_control_no = kwargs['violation_control_no']
        else:
            violation_control_no = 0

        if kwargs['electrical_inspection_no']:
            electrical_inspection_no = kwargs['electrical_inspection_no']
        else:
            electrical_inspection_no = 0

        if kwargs['sectional_occupancy']:
            sectional_occupancy = kwargs['sectional_occupancy']
        else:
            sectional_occupancy = 0

        if kwargs['occupant_load']:
            occupant_load = kwargs['occupant_load']
        else:
            occupant_load = 0

        if kwargs['egress_capacity']:
            egress_capacity = kwargs['egress_capacity']
        else:
            egress_capacity = 0

        if kwargs['any_renovation']:
            any_renovation = kwargs['any_renovation']
        else:
            any_renovation = 0

        if kwargs['renovation_specification']:
            renovation_specification = kwargs['renovation_specification']
        else:
            renovation_specification = 0

        if kwargs['horizontal_exit_capacity']:
            horizontal_exit_capacity = kwargs['horizontal_exit_capacity']
        else:
            horizontal_exit_capacity = 0

        if kwargs['exit_stair_capacity']:
            exit_stair_capacity = kwargs['exit_stair_capacity']
        else:
            exit_stair_capacity = 0

        if kwargs['no_of_exits']:
            no_of_exits = kwargs['no_of_exits']
        else:
            no_of_exits = 0

        if kwargs['is_exits_remote']:
            is_exits_remote = kwargs['is_exits_remote']
        else:
            is_exits_remote = 0

        if kwargs['exit_location']:
            exit_location = kwargs['exit_location']
        else:
            exit_location = 0

        if kwargs['any_enclosure']:
            any_enclosure = kwargs['any_enclosure']
        else:
            any_enclosure = 0

        if kwargs['is_exit_accessible']:
            is_exit_accessible = kwargs['is_exit_accessible']
        else:
            is_exit_accessible = 0

        if kwargs['is_fire_doors_provided']:
            is_fire_doors_provided = kwargs['is_fire_doors_provided']
        else:
            is_fire_doors_provided = 0

        if kwargs['self_closing_mechanism']:
            self_closing_mechanism = kwargs['self_closing_mechanism']
        else:
            self_closing_mechanism = 0

        if kwargs['panic_hardware']:
            panic_hardware = kwargs['panic_hardware']
        else:
            panic_hardware = 0

        if kwargs['readily_accessible']:
            readily_accessible = kwargs['readily_accessible']
        else:
            readily_accessible = 0

        if kwargs['travel_distance_within_limit']:
            travel_distance_within_limit = kwargs['travel_distance_within_limit']
        else:
            travel_distance_within_limit = 0

        if kwargs['adequate_illumination']:
            adequate_illumination = kwargs['adequate_illumination']
        else:
            adequate_illumination = 0

        if kwargs['panic_hardware_operational']:
            panic_hardware_operational = kwargs['panic_hardware_operational']
        else:
            panic_hardware_operational = 0

        if kwargs['doors_open_easily']:
            doors_open_easily = kwargs['doors_open_easily']
        else:
            doors_open_easily = 0

        if kwargs['bldg_with_mezzanine']:
            bldg_with_mezzanine = kwargs['bldg_with_mezzanine']
        else:
            bldg_with_mezzanine = 0

        if kwargs['is_obstructed']:
            is_obstructed = kwargs['is_obstructed']
        else:
            is_obstructed = 0

        if kwargs['dead_ends_within_limits']:
            dead_ends_within_limits = kwargs['dead_ends_within_limits']
        else:
            dead_ends_within_limits = 0

        if kwargs['proper_rating_illumination']:
            proper_rating_illumination = kwargs['proper_rating_illumination']
        else:
            proper_rating_illumination = 0

        if kwargs['door_swing_in_the_direction_of_exit']:
            door_swing_in_the_direction_of_exit = kwargs['door_swing_in_the_direction_of_exit']
        else:
            door_swing_in_the_direction_of_exit = 0

        if kwargs['self_closure_operational']:
            self_closure_operational = kwargs['self_closure_operational']
        else:
            self_closure_operational = 0

        if kwargs['mezzanine_with_proper_exits']:
            mezzanine_with_proper_exits = kwargs['mezzanine_with_proper_exits']
        else:
            mezzanine_with_proper_exits = 0

        if kwargs['corridors_of_sufficient_size']:
            corridors_of_sufficient_size = kwargs['corridors_of_sufficient_size']
        else:
            corridors_of_sufficient_size = 0

        if kwargs['main_stair_width']:
            main_stair_width = kwargs['main_stair_width']
        else:
            main_stair_width = 0

        if kwargs['construction']:
            construction = kwargs['construction']
        else:
            construction = 0

        if kwargs['main_stair_railings']:
            main_stair_railings = kwargs['main_stair_railings']
        else:
            main_stair_railings = 0

        if kwargs['main_stair_railings_built']:
            main_stair_railings_built = kwargs['main_stair_railings_built']
        else:
            main_stair_railings_built = 0

        if kwargs['main_stair_any_enclosure_provided']:
            main_stair_any_enclosure_provided = kwargs['main_stair_any_enclosure_provided']
        else:
            main_stair_any_enclosure_provided = 0

        if kwargs['enclosure_built']:
            enclosure_built = kwargs['enclosure_built']
        else:
            enclosure_built = 0

        if kwargs['any_openings']:
            any_openings = kwargs['any_openings']
        else:
            any_openings = 0

        if kwargs['main_stair_door_proper_rating']:
            main_stair_door_proper_rating = kwargs['main_stair_door_proper_rating']
        else:
            main_stair_door_proper_rating = 0

        if kwargs['main_stair_door_provided_with_vision_panel']:
            main_stair_door_provided_with_vision_panel = kwargs['main_stair_door_provided_with_vision_panel']
        else:
            main_stair_door_provided_with_vision_panel = 0

        if kwargs['main_stair_door_vision_panel_built']:
            main_stair_door_vision_panel_built = kwargs['main_stair_door_vision_panel_built']
        else:
            main_stair_door_vision_panel_built = 0

        if kwargs['main_stair_pressurized_stairway']:
            main_stair_pressurized_stairway = kwargs['main_stair_pressurized_stairway']
        else:
            main_stair_pressurized_stairway = 0

        if kwargs['main_stair_type_of_pressurized_stairway']:
            main_stair_type_of_pressurized_stairway = kwargs['main_stair_type_of_pressurized_stairway']
        else:
            main_stair_type_of_pressurized_stairway = 0

        if kwargs['fire_escape_count']:
            fire_escape_count = kwargs['fire_escape_count']
        else:
            fire_escape_count = 0

        if kwargs['fire_escape_width']:
            fire_escape_width = kwargs['fire_escape_width']
        else:
            fire_escape_width = 0

        if kwargs['fire_escape_construction']:
            fire_escape_construction = kwargs['fire_escape_construction']
        else:
            fire_escape_construction = 0

        if kwargs['fire_escape_railings']:
            fire_escape_railings = kwargs['fire_escape_railings']
        else:
            fire_escape_railings = 0

        if kwargs['fire_escape_built']:
            fire_escape_built = kwargs['fire_escape_built']
        else:
            fire_escape_built = 0

        if kwargs['fire_escape_location']:
            fire_escape_location = kwargs['fire_escape_location']
        else:
            fire_escape_location = 'None'

        if kwargs['fire_escape_obstruction']:
            fire_escape_obstruction = kwargs['fire_escape_obstruction']
        else:
            fire_escape_obstruction = 0

        if kwargs['discharge_of_exits']:
            discharge_of_exits = kwargs['discharge_of_exits']
        else:
            discharge_of_exits = 0

        if kwargs['fire_escape_any_enclosure_provided']:
            fire_escape_any_enclosure_provided = kwargs['fire_escape_any_enclosure_provided']
        else:
            fire_escape_any_enclosure_provided = 0

        if kwargs['fire_escape_enclosure']:
            fire_escape_enclosure = kwargs['fire_escape_enclosure']
        else:
            fire_escape_enclosure = 0

        if kwargs['fire_escape_opening']:
            fire_escape_opening = kwargs['fire_escape_opening']
        else:
            fire_escape_opening = 0

        if kwargs['fire_escape_opening_protected']:
            fire_escape_opening_protected = kwargs['fire_escape_opening_protected']
        else:
            fire_escape_opening_protected = 0

        if kwargs['fire_door_provided']:
            fire_door_provided = kwargs['fire_door_provided']
        else:
            fire_door_provided = 0

        if kwargs['fire_door_width']:
            fire_door_width = kwargs['fire_door_width']
        else:
            fire_door_width = 0

        if kwargs['fire_door_construction']:
            fire_door_construction = kwargs['fire_door_construction']
        else:
            fire_door_construction = 0

        if kwargs['fire_door_door_proper_rating']:
            fire_door_door_proper_rating = kwargs['fire_door_door_proper_rating']
        else:
            fire_door_door_proper_rating = 0

        if kwargs['fire_door_door_provided_with_vision_panel']:
            fire_door_door_provided_with_vision_panel = kwargs['fire_door_door_provided_with_vision_panel']
        else:
            fire_door_door_provided_with_vision_panel = 0

        if kwargs['fire_door_door_vision_panel_built']:
            fire_door_door_vision_panel_built = kwargs['fire_door_door_vision_panel_built']
        else:
            fire_door_door_vision_panel_built = 0

        if kwargs['fire_door_pressurized_stairway']:
            fire_door_pressurized_stairway = kwargs['fire_door_pressurized_stairway']
        else:
            fire_door_pressurized_stairway = 0

        if kwargs['fire_door_type_of_pressurized_stairway']:
            fire_door_type_of_pressurized_stairway = kwargs['fire_door_type_of_pressurized_stairway']
        else:
            fire_door_type_of_pressurized_stairway = 0

        if kwargs['horizontal_exit_width']:
            horizontal_exit_width = kwargs['horizontal_exit_width']
        else:
            horizontal_exit_width = 0

        if kwargs['horizontal_exit_construction']:
            horizontal_exit_construction = kwargs['horizontal_exit_construction']
        else:
            horizontal_exit_construction = 0

        if kwargs['horizontal_exit_vision_panel']:
            horizontal_exit_vision_panel = kwargs['horizontal_exit_vision_panel']
        else:
            horizontal_exit_vision_panel = 0

        if kwargs['horizontal_exit_door_swing_in_direction_of_egress']:
            horizontal_exit_door_swing_in_direction_of_egress = kwargs['horizontal_exit_door_swing_in_direction_of_egress']
        else:
            horizontal_exit_door_swing_in_direction_of_egress = 0

        if kwargs['horizontal_exit_with_self_closing_device']:
            horizontal_exit_with_self_closing_device = kwargs['horizontal_exit_with_self_closing_device']
        else:
            horizontal_exit_with_self_closing_device = 0

        if kwargs['horizontal_exit_corridor_width']:
            horizontal_exit_corridor_width = kwargs['horizontal_exit_corridor_width']
        else:
            horizontal_exit_corridor_width = 0

        if kwargs['horizontal_exit_corridor_construction']:
            horizontal_exit_corridor_construction = kwargs['horizontal_exit_corridor_construction']
        else:
            horizontal_exit_corridor_construction = 0

        if kwargs['horizontal_exit_corridor_walls_extended']:
            horizontal_exit_corridor_walls_extended = kwargs['horizontal_exit_corridor_walls_extended']
        else:
            horizontal_exit_corridor_walls_extended = 0

        if kwargs['horizontal_exit_properly_illuminated']:
            horizontal_exit_properly_illuminated = kwargs['horizontal_exit_properly_illuminated']
        else:
            horizontal_exit_properly_illuminated = 0

        if kwargs['horizontal_exit_readily_visible']:
            horizontal_exit_readily_visible = kwargs['horizontal_exit_readily_visible']
        else:
            horizontal_exit_readily_visible = 0

        if kwargs['horizontal_exit_properly_marked']:
            horizontal_exit_properly_marked = kwargs['horizontal_exit_properly_marked']
        else:
            horizontal_exit_properly_marked = 0

        if kwargs['horizontal_exit_with_illuminated_directional_sign']:
            horizontal_exit_with_illuminated_directional_sign = kwargs['horizontal_exit_with_illuminated_directional_sign']
        else:
            horizontal_exit_with_illuminated_directional_sign = 0

        if kwargs['horizontal_exit_properly_located']:
            horizontal_exit_properly_located = kwargs['horizontal_exit_properly_located']
        else:
            horizontal_exit_properly_located = 0

        if kwargs['ramps_provided']:
            ramps_provided = kwargs['ramps_provided']
        else:
            ramps_provided = 0

        if kwargs['ramps_type']:
            ramps_type = kwargs['ramps_type']
        else:
            ramps_type = 'None'

        if kwargs['ramps_width']:
            ramps_width = kwargs['ramps_width']
        else:
            ramps_width = 0

        if kwargs['ramps_class']:
            ramps_class = kwargs['ramps_class']
        else:
            ramps_class = 0

        if kwargs['ramps_railing_provided']:
            ramps_railing_provided = kwargs['ramps_railing_provided']
        else:
            ramps_railing_provided = 0

        if kwargs['ramps_height']:
            ramps_height = kwargs['ramps_height']
        else:
            ramps_height = 0

        if kwargs['ramps_enclosure']:
            ramps_enclosure = kwargs['ramps_enclosure']
        else:
            ramps_enclosure = 0

        if kwargs['ramps_construction']:
            ramps_construction = kwargs['ramps_construction']
        else:
            ramps_construction = 0

        if kwargs['ramps_fire_doors']:
            ramps_fire_doors = kwargs['ramps_fire_doors']
        else:
            ramps_fire_doors = 0

        if kwargs['ramps_fire_doors_width']:
            ramps_fire_doors_width = kwargs['ramps_fire_doors_width']
        else:
            ramps_fire_doors_width = 0

        if kwargs['ramps_fire_doors_construction']:
            ramps_fire_doors_construction = kwargs['ramps_fire_doors_construction']
        else:
            ramps_fire_doors_construction = 0

        if kwargs['ramps_with_self_closing_device']:
            ramps_with_self_closing_device = kwargs['ramps_with_self_closing_device']
        else:
            ramps_with_self_closing_device = 0

        if kwargs['ramps_door_with_proper_rating']:
            ramps_door_with_proper_rating = kwargs['ramps_door_with_proper_rating']
        else:
            ramps_door_with_proper_rating = 0

        if kwargs['ramps_door_with_vision_panel']:
            ramps_door_with_vision_panel = kwargs['ramps_door_with_vision_panel']
        else:
            ramps_door_with_vision_panel = 0

        if kwargs['ramps_door_vision_panel_built']:
            ramps_door_vision_panel_built = kwargs['ramps_door_vision_panel_built']
        else:
            ramps_door_vision_panel_built = 0

        if kwargs['ramps_door_swing_in_direction_of_egress']:
            ramps_door_swing_in_direction_of_egress = kwargs['ramps_door_swing_in_direction_of_egress']
        else:
            ramps_door_swing_in_direction_of_egress = 0

        if kwargs['ramps_obstruction']:
            ramps_obstruction = kwargs['ramps_obstruction']
        else:
            ramps_obstruction = 0

        if kwargs['ramps_discharge_of_exit']:
            ramps_discharge_of_exit = kwargs['ramps_discharge_of_exit']
        else:
            ramps_discharge_of_exit = 0

        if kwargs['safe_refuge_provided']:
            safe_refuge_provided = kwargs['safe_refuge_provided']
        else:
            safe_refuge_provided = 0

        if kwargs['safe_refuge_type']:
            safe_refuge_type = kwargs['safe_refuge_type']
        else:
            safe_refuge_type = 'None'

        if kwargs['safe_refuge_enclosure']:
            safe_refuge_enclosure = kwargs['safe_refuge_enclosure']
        else:
            safe_refuge_enclosure = 0

        if kwargs['safe_refuge_construction']:
            safe_refuge_construction = kwargs['safe_refuge_construction']
        else:
            safe_refuge_construction = 0

        if kwargs['safe_refuge_fire_door']:
            safe_refuge_fire_door = kwargs['safe_refuge_fire_door']
        else:
            safe_refuge_fire_door = 0

        if kwargs['safe_refuge_fire_door_width']:
            safe_refuge_fire_door_width = kwargs['safe_refuge_fire_door_width']
        else:
            safe_refuge_fire_door_width = 0

        if kwargs['safe_refuge_fire_door_construction']:
            safe_refuge_fire_door_construction = kwargs['safe_refuge_fire_door_construction']
        else:
            safe_refuge_fire_door_construction = 0

        if kwargs['safe_refuge_with_self_closing_device']:
            safe_refuge_with_self_closing_device = kwargs['safe_refuge_with_self_closing_device']
        else:
            safe_refuge_with_self_closing_device = 0

        if kwargs['safe_refuge_door_proper_rating']:
            safe_refuge_door_proper_rating = kwargs['safe_refuge_door_proper_rating']
        else:
            safe_refuge_door_proper_rating = 0

        if kwargs['safe_refuge_with_vision_panel']:
            safe_refuge_with_vision_panel = kwargs['safe_refuge_with_vision_panel']
        else:
            safe_refuge_with_vision_panel = 0

        if kwargs['safe_refuge_vision_panel_built']:
            safe_refuge_vision_panel_built = kwargs['safe_refuge_vision_panel_built']
        else:
            safe_refuge_vision_panel_built = 0

        if kwargs['safe_refuge_swing_in_direction_of_egress']:
            safe_refuge_swing_in_direction_of_egress = kwargs['safe_refuge_swing_in_direction_of_egress']
        else:
            safe_refuge_swing_in_direction_of_egress = 0

        if kwargs['emergency_light']:
            emergency_light = kwargs['emergency_light']
        else:
            emergency_light = 0

        if kwargs['emergency_light_source']:
            emergency_light_source = kwargs['emergency_light_source']
        else:
            emergency_light_source = 'None'

        if kwargs['emergency_light_per_floor_count']:
            emergency_light_per_floor_count = kwargs['emergency_light_per_floor_count']
        else:
            emergency_light_per_floor_count = 0

        if kwargs['emergency_light_hallway_count']:
            emergency_light_hallway_count = kwargs['emergency_light_hallway_count']
        else:
            emergency_light_hallway_count = 0

        if kwargs['emergency_light_stairway_count']:
            emergency_light_stairway_count = kwargs['emergency_light_stairway_count']
        else:
            emergency_light_stairway_count = 0

        if kwargs['emergency_light_operational']:
            emergency_light_operational = kwargs['emergency_light_operational']
        else:
            emergency_light_operational = 0

        if kwargs['emergency_light_exit_path_properly_illuminated']:
            emergency_light_exit_path_properly_illuminated = kwargs['emergency_light_exit_path_properly_illuminated']
        else:
            emergency_light_exit_path_properly_illuminated = 0

        if kwargs['emergency_light_tested_monthly']:
            emergency_light_tested_monthly = kwargs['emergency_light_tested_monthly']
        else:
            emergency_light_tested_monthly = 0

        if kwargs['exit_signs_illuminated']:
            exit_signs_illuminated = kwargs['exit_signs_illuminated']
        else:
            exit_signs_illuminated = 0

        if kwargs['exit_signs_location']:
            exit_signs_location = kwargs['exit_signs_location']
        else:
            exit_signs_location = 0

        if kwargs['exit_signs_source']:
            exit_signs_source = kwargs['exit_signs_source']
        else:
            exit_signs_source = 'None'

        if kwargs['exit_signs_visible']:
            exit_signs_visible = kwargs['exit_signs_visible']
        else:
            exit_signs_visible = 0

        if kwargs['exit_signs_min_letter_size']:
            exit_signs_min_letter_size = kwargs['exit_signs_min_letter_size']
        else:
            exit_signs_min_letter_size = 0

        if kwargs['exit_route_posted_on_lobby']:
            exit_route_posted_on_lobby = kwargs['exit_route_posted_on_lobby']
        else:
            exit_route_posted_on_lobby = 0

        if kwargs['exit_route_posted_on_rooms']:
            exit_route_posted_on_rooms = kwargs['exit_route_posted_on_rooms']
        else:
            exit_route_posted_on_rooms = 0

        if kwargs['directional_exit_signs']:
            directional_exit_signs = kwargs['directional_exit_signs']
        else:
            directional_exit_signs = 0

        if kwargs['directional_exit_signs_location']:
            directional_exit_signs_location = kwargs['directional_exit_signs_location']
        else:
            directional_exit_signs_location = 0

        if kwargs['no_smoking_sign']:
            no_smoking_sign = kwargs['no_smoking_sign']
        else:
            no_smoking_sign = 0

        if kwargs['dead_end_sign']:
            dead_end_sign = kwargs['dead_end_sign']
        else:
            dead_end_sign = 0

        if kwargs['elevator_sign']:
            elevator_sign = kwargs['elevator_sign']
        else:
            elevator_sign = 0

        if kwargs['keep_door_closed_sign']:
            keep_door_closed_sign = kwargs['keep_door_closed_sign']
        else:
            keep_door_closed_sign = 0

        if kwargs['others']:
            others = kwargs['others']
        else:
            others = 0

        if kwargs['vertical_openings_properly_protected']:
            vertical_openings_properly_protected = kwargs['vertical_openings_properly_protected']
        else:
            vertical_openings_properly_protected = 0

        if kwargs['vertical_openings_atrium']:
            vertical_openings_atrium = kwargs['vertical_openings_atrium']
        else:
            vertical_openings_atrium = 0

        if kwargs['fire_doors_good_condition']:
            fire_doors_good_condition = kwargs['fire_doors_good_condition']
        else:
            fire_doors_good_condition = 0

        if kwargs['elevator_opening_protected']:
            elevator_opening_protected = kwargs['elevator_opening_protected']
        else:
            elevator_opening_protected = 0

        if kwargs['pipe_chase_opening_protected']:
            pipe_chase_opening_protected = kwargs['pipe_chase_opening_protected']
        else:
            pipe_chase_opening_protected = 0

        if kwargs['aircon_ducts_with_dumper']:
            aircon_ducts_with_dumper = kwargs['aircon_ducts_with_dumper']
        else:
            aircon_ducts_with_dumper = 0

        if kwargs['garbage_chute_protected']:
            garbage_chute_protected = kwargs['garbage_chute_protected']
        else:
            garbage_chute_protected = 0

        if kwargs['between_floor_protected']:
            between_floor_protected = kwargs['between_floor_protected']
        else:
            between_floor_protected = 0

        if kwargs['standpipe_type']:
            standpipe_type = kwargs['standpipe_type']
        else:
            standpipe_type = 'None'

        if kwargs['standpipe_tank_capacity']:
            standpipe_tank_capacity = kwargs['standpipe_tank_capacity']
        else:
            standpipe_tank_capacity = 0

        if kwargs['standpipe_location']:
            standpipe_location = kwargs['standpipe_location']
        else:
            standpipe_location = 0

        if kwargs['siamese_intake_provided']:
            siamese_intake_provided = kwargs['siamese_intake_provided']
        else:
            siamese_intake_provided = 0

        if kwargs['siamese_intake_location']:
            siamese_intake_location = kwargs['siamese_intake_location']
        else:
            siamese_intake_location = 0

        if kwargs['siamese_intake_size']:
            siamese_intake_size = kwargs['siamese_intake_size']
        else:
            siamese_intake_size = 0

        if kwargs['siamese_intake_count']:
            siamese_intake_count = kwargs['siamese_intake_count']
        else:
            siamese_intake_count = 0

        if kwargs['siamese_intake_accessible']:
            siamese_intake_accessible = kwargs['siamese_intake_accessible']
        else:
            siamese_intake_accessible = 0

        if kwargs['fire_hose_cabinet']:
            fire_hose_cabinet = kwargs['fire_hose_cabinet']
        else:
            fire_hose_cabinet = 0

        if kwargs['fire_hose_cabinet_accessories']:
            fire_hose_cabinet_accessories = kwargs['fire_hose_cabinet_accessories']
        else:
            fire_hose_cabinet_accessories = 0

        if kwargs['fire_hose_cabinet_location']:
            fire_hose_cabinet_location = kwargs['fire_hose_cabinet_location']
        else:
            fire_hose_cabinet_location = 0

        if kwargs['fire_hose_per_floor_count']:
            fire_hose_per_floor_count = kwargs['fire_hose_per_floor_count']
        else:
            fire_hose_per_floor_count = 0

        if kwargs['fire_hose_size']:
            fire_hose_size = kwargs['fire_hose_size']
        else:
            fire_hose_size = 0

        if kwargs['fire_hose_length']:
            fire_hose_length = kwargs['fire_hose_length']
        else:
            fire_hose_length = 0

        if kwargs['fire_hose_nozzle']:
            fire_hose_nozzle = kwargs['fire_hose_nozzle']
        else:
            fire_hose_nozzle = 0

        if kwargs['fire_lane']:
            fire_lane = kwargs['fire_lane']
        else:
            fire_lane = 0

        if kwargs['fire_hydrant_location']:
            fire_hydrant_location = kwargs['fire_hydrant_location']
        else:
            fire_hydrant_location = 0

        if kwargs['portable_fire_extinguisher_type']:
            portable_fire_extinguisher_type = kwargs['portable_fire_extinguisher_type']
        else:
            portable_fire_extinguisher_type = 0

        if kwargs['portable_fire_extinguisher_capacity']:
            portable_fire_extinguisher_capacity = kwargs['portable_fire_extinguisher_capacity']
        else:
            portable_fire_extinguisher_capacity = 0

        if kwargs['portable_fire_extinguisher_count']:
            portable_fire_extinguisher_count = kwargs['portable_fire_extinguisher_count']
        else:
            portable_fire_extinguisher_count = 0

        if kwargs['portable_fire_extinguisher_with_ps_mark']:
            portable_fire_extinguisher_with_ps_mark = kwargs['portable_fire_extinguisher_with_ps_mark']
        else:
            portable_fire_extinguisher_with_ps_mark = 0

        if kwargs['portable_fire_extinguisher_with_iso_mark']:
            portable_fire_extinguisher_with_iso_mark = kwargs['portable_fire_extinguisher_with_iso_mark']
        else:
            portable_fire_extinguisher_with_iso_mark = 0

        if kwargs['portable_fire_extinguisher_maintained']:
            portable_fire_extinguisher_maintained = kwargs['portable_fire_extinguisher_maintained']
        else:
            portable_fire_extinguisher_maintained = 0

        if kwargs['portable_fire_extinguisher_conspicuously_located']:
            portable_fire_extinguisher_conspicuously_located = kwargs['portable_fire_extinguisher_conspicuously_located']
        else:
            portable_fire_extinguisher_conspicuously_located = 0

        if kwargs['portable_fire_extinguisher_accessible']:
            portable_fire_extinguisher_accessible = kwargs['portable_fire_extinguisher_accessible']
        else:
            portable_fire_extinguisher_accessible = 0

        if kwargs['portable_fire_extinguisher_other_type']:
            portable_fire_extinguisher_other_type = kwargs['portable_fire_extinguisher_other_type']
        else:
            portable_fire_extinguisher_other_type = 0

        if kwargs['sprinkler_system_agent_used']:
            sprinkler_system_agent_used = kwargs['sprinkler_system_agent_used']
        else:
            sprinkler_system_agent_used = 0

        if kwargs['jockey_pump_capacity']:
            jockey_pump_capacity = kwargs['jockey_pump_capacity']
        else:
            jockey_pump_capacity = 0

        if kwargs['fire_pump_capacity']:
            fire_pump_capacity = kwargs['fire_pump_capacity']
        else:
            fire_pump_capacity = 0

        if kwargs['gpm_tank_capacity']:
            gpm_tank_capacity = kwargs['gpm_tank_capacity']
        else:
            gpm_tank_capacity = 0

        if kwargs['maintaining_line_pressure']:
            maintaining_line_pressure = kwargs['maintaining_line_pressure']
        else:
            maintaining_line_pressure = 0

        if kwargs['farthest_sprinkler_head_pressure']:
            farthest_sprinkler_head_pressure = kwargs['farthest_sprinkler_head_pressure']
        else:
            farthest_sprinkler_head_pressure = 0

        if kwargs['riser_size']:
            riser_size = kwargs['riser_size']
        else:
            riser_size = 0

        if kwargs['type_of_heads_installed']:
            type_of_heads_installed = kwargs['type_of_heads_installed']
        else:
            type_of_heads_installed = 0

        if kwargs['heads_per_floor_count']:
            heads_per_floor_count = kwargs['heads_per_floor_count']
        else:
            heads_per_floor_count = 0

        if kwargs['heads_total_count']:
            heads_total_count = kwargs['heads_total_count']
        else:
            heads_total_count = 0

        if kwargs['spacing_of_heads']:
            spacing_of_heads = kwargs['spacing_of_heads']
        else:
            spacing_of_heads = 0

        if kwargs['location_of_fire_dept_connection']:
            location_of_fire_dept_connection = kwargs['location_of_fire_dept_connection']
        else:
            location_of_fire_dept_connection = 0

        if kwargs['plan_submitted']:
            plan_submitted = kwargs['plan_submitted']
        else:
            plan_submitted = 0

        if kwargs['firewall_required']:
            firewall_required = kwargs['firewall_required']
        else:
            firewall_required = 0

        if kwargs['firewall_provided']:
            firewall_provided = kwargs['firewall_provided']
        else:
            firewall_provided = 0

        if kwargs['firewall_opening']:
            firewall_opening = kwargs['firewall_opening']
        else:
            firewall_opening = 0

        if kwargs['boiler_provided']:
            boiler_provided = kwargs['boiler_provided']
        else:
            boiler_provided = 0

        if kwargs['boiler_unit_count']:
            boiler_unit_count = kwargs['boiler_unit_count']
        else:
            boiler_unit_count = 0

        if kwargs['boiler_fuel']:
            boiler_fuel = kwargs['boiler_fuel']
        else:
            boiler_fuel = 'None'

        if kwargs['boiler_capacity']:
            boiler_capacity = kwargs['boiler_capacity']
        else:
            boiler_capacity = 0

        if kwargs['boiler_container']:
            boiler_container = kwargs['boiler_container']
        else:
            boiler_container = 'None'

        if kwargs['boiler_location']:
            boiler_location = kwargs['boiler_location']
        else:
            boiler_location = 0

        if kwargs['lpg_installation_with_permit']:
            lpg_installation_with_permit = kwargs['lpg_installation_with_permit']
        else:
            lpg_installation_with_permit = 0

        if kwargs['fuel_with_storage_permit']:
            fuel_with_storage_permit = kwargs['fuel_with_storage_permit']
        else:
            fuel_with_storage_permit = 0

        if kwargs['generator_set']:
            generator_set = kwargs['generator_set']
        else:
            generator_set = 0

        if kwargs['generator_set_type']:
            generator_set_type = kwargs['generator_set_type']
        else:
            generator_set_type = 'None'

        if kwargs['generator_fuel']:
            generator_fuel = kwargs['generator_fuel']
        else:
            generator_fuel = 'None'

        if kwargs['generator_capacity']:
            generator_capacity = kwargs['generator_capacity']
        else:
            generator_capacity = 0

        if kwargs['generator_location']:
            generator_location = kwargs['generator_location']
        else:
            generator_location = 0

        if kwargs['generator_bound_on_wall']:
            generator_bound_on_wall = kwargs['generator_bound_on_wall']
        else:
            generator_bound_on_wall = 0

        if kwargs['generator_container']:
            generator_container = kwargs['generator_container']
        else:
            generator_container = 'None'

        if kwargs['generator_dispensing_system']:
            generator_dispensing_system = kwargs['generator_dispensing_system']
        else:
            generator_dispensing_system = 'None'

        if kwargs['generator_output_capacity']:
            generator_output_capacity = kwargs['generator_output_capacity']
        else:
            generator_output_capacity = 0

        if kwargs['generator_mechanical_permit']:
            generator_mechanical_permit = kwargs['generator_mechanical_permit']
        else:
            generator_mechanical_permit = 0

        if kwargs['generator_fuel_storage_permit']:
            generator_fuel_storage_permit = kwargs['generator_fuel_storage_permit']
        else:
            generator_fuel_storage_permit = 0

        if kwargs['generator_others']:
            generator_others = kwargs['generator_others']
        else:
            generator_others = 0

        if kwargs['generator_automatic_transfer_switch']:
            generator_automatic_transfer_switch = kwargs['generator_automatic_transfer_switch']
        else:
            generator_automatic_transfer_switch = 0

        if kwargs['generator_time_interval']:
            generator_time_interval = kwargs['generator_time_interval']
        else:
            generator_time_interval = None

        if kwargs['refuse_handling']:
            refuse_handling = kwargs['refuse_handling']
        else:
            refuse_handling = 0

        if kwargs['refuse_handling_enclosure']:
            refuse_handling_enclosure = kwargs['refuse_handling_enclosure']
        else:
            refuse_handling_enclosure = 0

        if kwargs['refuse_handling_fire_protection']:
            refuse_handling_fire_protection = kwargs['refuse_handling_fire_protection']
        else:
            refuse_handling_fire_protection = 0

        if kwargs['electrical_hazard']:
            electrical_hazard = kwargs['electrical_hazard']
        else:
            electrical_hazard = 0

        if kwargs['electrical_hazard_location']:
            electrical_hazard_location = kwargs['electrical_hazard_location']
        else:
            electrical_hazard_location = 0

        if kwargs['mechanical_hazard']:
            mechanical_hazard = kwargs['mechanical_hazard']
        else:
            mechanical_hazard = 0

        if kwargs['mechanical_hazard_location']:
            mechanical_hazard_location = kwargs['mechanical_hazard_location']
        else:
            mechanical_hazard_location = 0

        if kwargs['elevator_count']:
            elevator_count = kwargs['elevator_count']
        else:
            elevator_count = 0

        if kwargs['other_service_system']:
            other_service_system = kwargs['other_service_system']
        else:
            other_service_system = 'None'

        if kwargs['hazardous_area']:
            hazardous_area = kwargs['hazardous_area']
        else:
            hazardous_area = 'None'

        if kwargs['hazardous_area_other']:
            hazardous_area_other = kwargs['hazardous_area_other']
        else:
            hazardous_area_other = 0

        if kwargs['separation_fire_rated']:
            separation_fire_rated = kwargs['separation_fire_rated']
        else:
            separation_fire_rated = 0

        if kwargs['type_of_protection']:
            type_of_protection = kwargs['type_of_protection']
        else:
            type_of_protection = 0

        if kwargs['separation_fire_rated_count']:
            separation_fire_rated_count = kwargs['separation_fire_rated_count']
        else:
            separation_fire_rated_count = 0

        if kwargs['separation_fire_rated_accessible']:
            separation_fire_rated_accessible = kwargs['separation_fire_rated_accessible']
        else:
            separation_fire_rated_accessible = 0

        if kwargs['separation_fire_rated_fuel']:
            separation_fire_rated_fuel = kwargs['separation_fire_rated_fuel']
        else:
            separation_fire_rated_fuel = 0

        if kwargs['separation_fire_rated_location']:
            separation_fire_rated_location = kwargs['separation_fire_rated_location']
        else:
            separation_fire_rated_location = 0

        if kwargs['separation_fire_rated_permit']:
            separation_fire_rated_permit = kwargs['separation_fire_rated_permit']
        else:
            separation_fire_rated_permit = 0

        if kwargs['hazardous_material']:
            hazardous_material = kwargs['hazardous_material']
        else:
            hazardous_material = 0

        if kwargs['hazardous_material_stored']:
            hazardous_material_stored = kwargs['hazardous_material_stored']
        else:
            hazardous_material_stored = 0

        if kwargs['fire_brigade_organization']:
            fire_brigade_organization = kwargs['fire_brigade_organization']
        else:
            fire_brigade_organization = 0

        if kwargs['fire_safety_seminar']:
            fire_safety_seminar = kwargs['fire_safety_seminar']
        else:
            fire_safety_seminar = 0

        if kwargs['employee_trained_in_emergency_procedures']:
            employee_trained_in_emergency_procedures = kwargs['employee_trained_in_emergency_procedures']
        else:
            employee_trained_in_emergency_procedures = 0

        if kwargs['evacuation_drill_first']:
            evacuation_drill_first = kwargs['evacuation_drill_first']
        else:
            evacuation_drill_first = 0

        if kwargs['evacuation_drill_second']:
            evacuation_drill_second = kwargs['evacuation_drill_second']
        else:
            evacuation_drill_second = 0

        if kwargs['defects']:
            defects = kwargs['defects']
        else:
            defects = 0

        if kwargs['defects_photo']:
            defects_photo = kwargs['defects_photo']
        else:
            defects_photo = 0

        if kwargs['recommendations']:
            recommendations = kwargs['recommendations']
        else:
            recommendations = 0

        if kwargs['building']:
            building = kwargs['building']
        else:
            building = 0

        if kwargs['business']:
            business = kwargs['business']
        else:
            business = 0

        if kwargs['building_permit_date_issued']:
            building_permit_date_issued = kwargs['building_permit_date_issued']
        else:
            building_permit_date_issued = None

        if kwargs['occupancy_permit_date_issued']:
            occupancy_permit_date_issued = kwargs['occupancy_permit_date_issued']
        else:
            occupancy_permit_date_issued = None

        if kwargs['fsic_date_issued']:
            fsic_date_issued = kwargs['fsic_date_issued']
        else:
            fsic_date_issued = None

        if kwargs['fire_drill_certificate_date_issued']:
            fire_drill_certificate_date_issued = kwargs['fire_drill_certificate_date_issued']
        else:
            fire_drill_certificate_date_issued = None

        if kwargs['violation_control_no_date_issued']:
            violation_control_no_date_issued = kwargs['violation_control_no_date_issued']
        else:
            violation_control_no_date_issued = None

        if kwargs['electrical_inspection_date_issued']:
            electrical_inspection_date_issued = kwargs['electrical_inspection_date_issued']
        else:
            electrical_inspection_date_issued = None

        if kwargs['insurance_date_issued']:
            insurance_date_issued = kwargs['insurance_date_issued']
        else:
            insurance_date_issued = None

        if kwargs['main_stair_pressurized_stairway_last_tested']:
            main_stair_pressurized_stairway_last_tested = kwargs['main_stair_pressurized_stairway_last_tested']
        else:
            main_stair_pressurized_stairway_last_tested = None

        if kwargs['fire_door_pressurized_stairway_last_tested']:
            fire_door_pressurized_stairway_last_tested = kwargs['fire_door_pressurized_stairway_last_tested']
        else:
            fire_door_pressurized_stairway_last_tested = None

        if kwargs['vertical_opening_last_tested']:
            vertical_opening_last_tested = kwargs['vertical_opening_last_tested']
        else:
            vertical_opening_last_tested = None

        if kwargs['fire_hose_last_tested']:
            fire_hose_last_tested = kwargs['fire_hose_last_tested']
        else:
            fire_hose_last_tested = None

        if kwargs['sprinkler_system_last_tested']:
            sprinkler_system_last_tested = kwargs['sprinkler_system_last_tested']
        else:
            sprinkler_system_last_tested = None

        if kwargs['sprinkler_system_last_conducted']:
            sprinkler_system_last_conducted = kwargs['sprinkler_system_last_conducted']
        else:
            sprinkler_system_last_conducted = None

        if kwargs['certificate_of_installation_date']:
            certificate_of_installation_date = kwargs['certificate_of_installation_date']
        else:
            certificate_of_installation_date =None

        if kwargs['generator_mechanical_permit_date_issued']:
            generator_mechanical_permit_date_issued = kwargs['generator_mechanical_permit_date_issued']
        else:
            generator_mechanical_permit_date_issued = None


        if flag:
            checklist = self.model(
                first_name=kwargs['first_name'],
                middle_name=kwargs['middle_name'],
                last_name=kwargs['last_name'],
                policy_no=policy_no,
                building_permit=building_permit,
                occupancy_permit=occupancy_permit,
                fsic_control_no=fsic_control_no,
                fsic_fee=fsic_fee,
                fire_drill_certificate=fire_drill_certificate,
                violation_control_no=violation_control_no,
                electrical_inspection_no=electrical_inspection_no,
                sectional_occupancy=sectional_occupancy,
                occupant_load=occupant_load,
                egress_capacity=egress_capacity,
                any_renovation=any_renovation,
                renovation_specification=renovation_specification,
                horizontal_exit_capacity=horizontal_exit_capacity,
                exit_stair_capacity=exit_stair_capacity,
                no_of_exits=no_of_exits,
                is_exits_remote=is_exits_remote,
                exit_location=exit_location,
                any_enclosure=any_enclosure,
                is_exit_accessible=is_exit_accessible,
                is_fire_doors_provided=is_fire_doors_provided,
                self_closing_mechanism=self_closing_mechanism,
                panic_hardware=panic_hardware,
                readily_accessible=readily_accessible,
                travel_distance_within_limit=travel_distance_within_limit,
                adequate_illumination=adequate_illumination,
                panic_hardware_operational=panic_hardware_operational,
                doors_open_easily=doors_open_easily,
                bldg_with_mezzanine=bldg_with_mezzanine,
                is_obstructed=is_obstructed,
                dead_ends_within_limits=dead_ends_within_limits,
                proper_rating_illumination=proper_rating_illumination,
                door_swing_in_the_direction_of_exit=door_swing_in_the_direction_of_exit,
                self_closure_operational=self_closure_operational,
                mezzanine_with_proper_exits=mezzanine_with_proper_exits,
                corridors_of_sufficient_size=corridors_of_sufficient_size,
                main_stair_width=main_stair_width,
                construction=construction,
                main_stair_railings=main_stair_railings,
                main_stair_railings_built=main_stair_railings_built,
                main_stair_any_enclosure_provided=main_stair_any_enclosure_provided,
                enclosure_built=enclosure_built,
                any_openings=any_openings,
                main_stair_door_proper_rating=main_stair_door_proper_rating,
                main_stair_door_provided_with_vision_panel=main_stair_door_provided_with_vision_panel,
                main_stair_door_vision_panel_built=main_stair_door_vision_panel_built,
                main_stair_pressurized_stairway=main_stair_pressurized_stairway,
                main_stair_type_of_pressurized_stairway=main_stair_type_of_pressurized_stairway,
                fire_escape_count=fire_escape_count,
                fire_escape_width=fire_escape_width,
                fire_escape_construction=fire_escape_construction,
                fire_escape_railings=fire_escape_railings,
                fire_escape_built=fire_escape_built,
                fire_escape_location=fire_escape_location,
                fire_escape_obstruction=fire_escape_obstruction,
                discharge_of_exits=discharge_of_exits,
                fire_escape_any_enclosure_provided=fire_escape_any_enclosure_provided,
                fire_escape_enclosure=fire_escape_enclosure,
                fire_escape_opening=fire_escape_opening,
                fire_escape_opening_protected=fire_escape_opening_protected,
                fire_door_provided=fire_door_provided,
                fire_door_width=fire_door_width,
                fire_door_construction=fire_door_construction,
                fire_door_door_proper_rating=fire_door_door_proper_rating,
                fire_door_door_provided_with_vision_panel=fire_door_door_provided_with_vision_panel,
                fire_door_door_vision_panel_built=fire_door_door_vision_panel_built,
                fire_door_pressurized_stairway=fire_door_pressurized_stairway,
                fire_door_type_of_pressurized_stairway=fire_door_type_of_pressurized_stairway,
                horizontal_exit_width=horizontal_exit_width,
                horizontal_exit_construction=horizontal_exit_construction,
                horizontal_exit_vision_panel=horizontal_exit_vision_panel,
                horizontal_exit_door_swing_in_direction_of_egress=horizontal_exit_door_swing_in_direction_of_egress,
                horizontal_exit_with_self_closing_device=horizontal_exit_with_self_closing_device,
                horizontal_exit_corridor_width=horizontal_exit_corridor_width,
                horizontal_exit_corridor_construction=horizontal_exit_corridor_construction,
                horizontal_exit_corridor_walls_extended=horizontal_exit_corridor_walls_extended,
                horizontal_exit_properly_illuminated=horizontal_exit_properly_illuminated,
                horizontal_exit_readily_visible=horizontal_exit_readily_visible,
                horizontal_exit_properly_marked=horizontal_exit_properly_marked,
                horizontal_exit_with_illuminated_directional_sign=horizontal_exit_with_illuminated_directional_sign,
                horizontal_exit_properly_located=horizontal_exit_properly_located,
                ramps_provided=ramps_provided,
                ramps_type=ramps_type,
                ramps_width=ramps_width,
                ramps_class=ramps_class,
                ramps_railing_provided=ramps_railing_provided,
                ramps_height=ramps_height,
                ramps_enclosure=ramps_enclosure,
                ramps_construction=ramps_construction,
                ramps_fire_doors=ramps_fire_doors,
                ramps_fire_doors_width=ramps_fire_doors_width,
                ramps_fire_doors_construction=ramps_fire_doors_construction,
                ramps_with_self_closing_device=ramps_with_self_closing_device,
                ramps_door_with_proper_rating=ramps_door_with_proper_rating,
                ramps_door_with_vision_panel=ramps_door_with_vision_panel,
                ramps_door_vision_panel_built=ramps_door_vision_panel_built,
                ramps_door_swing_in_direction_of_egress=ramps_door_swing_in_direction_of_egress,
                ramps_obstruction=ramps_obstruction,
                ramps_discharge_of_exit=ramps_discharge_of_exit,
                safe_refuge_provided=safe_refuge_provided,
                safe_refuge_type=safe_refuge_type,
                safe_refuge_enclosure=safe_refuge_enclosure,
                safe_refuge_construction=safe_refuge_construction,
                safe_refuge_fire_door=safe_refuge_fire_door,
                safe_refuge_fire_door_width=safe_refuge_fire_door_width,
                safe_refuge_fire_door_construction=safe_refuge_fire_door_construction,
                safe_refuge_with_self_closing_device=safe_refuge_with_self_closing_device,
                safe_refuge_door_proper_rating=safe_refuge_door_proper_rating,
                safe_refuge_with_vision_panel=safe_refuge_with_vision_panel,
                safe_refuge_vision_panel_built=safe_refuge_vision_panel_built,
                safe_refuge_swing_in_direction_of_egress=safe_refuge_swing_in_direction_of_egress,
                emergency_light=emergency_light,
                emergency_light_source=emergency_light_source,
                emergency_light_per_floor_count=emergency_light_per_floor_count,
                emergency_light_hallway_count=emergency_light_hallway_count,
                emergency_light_stairway_count=emergency_light_stairway_count,
                emergency_light_operational=emergency_light_operational,
                emergency_light_exit_path_properly_illuminated=emergency_light_exit_path_properly_illuminated,
                emergency_light_tested_monthly=emergency_light_tested_monthly,
                exit_signs_illuminated=exit_signs_illuminated,
                exit_signs_location=exit_signs_location,
                exit_signs_source=exit_signs_source,
                exit_signs_visible=exit_signs_visible,
                exit_signs_min_letter_size=exit_signs_min_letter_size,
                exit_route_posted_on_lobby=exit_route_posted_on_lobby,
                exit_route_posted_on_rooms=exit_route_posted_on_rooms,
                directional_exit_signs=directional_exit_signs,
                directional_exit_signs_location=directional_exit_signs_location,
                no_smoking_sign=no_smoking_sign,
                dead_end_sign=dead_end_sign,
                elevator_sign=elevator_sign,
                keep_door_closed_sign=keep_door_closed_sign,
                others=others,
                vertical_openings_properly_protected=vertical_openings_properly_protected,
                vertical_openings_atrium=vertical_openings_atrium,
                fire_doors_good_condition=fire_doors_good_condition,
                elevator_opening_protected=elevator_opening_protected,
                pipe_chase_opening_protected=pipe_chase_opening_protected,
                aircon_ducts_with_dumper=aircon_ducts_with_dumper,
                garbage_chute_protected=garbage_chute_protected,
                between_floor_protected=between_floor_protected,
                standpipe_type=standpipe_type,
                standpipe_tank_capacity=standpipe_tank_capacity,
                standpipe_location=standpipe_location,
                siamese_intake_provided=siamese_intake_provided,
                siamese_intake_location=siamese_intake_location,
                siamese_intake_size=siamese_intake_size,
                siamese_intake_count=siamese_intake_count,
                siamese_intake_accessible=siamese_intake_accessible,
                fire_hose_cabinet=fire_hose_cabinet,
                fire_hose_cabinet_accessories=fire_hose_cabinet_accessories,
                fire_hose_cabinet_location=fire_hose_cabinet_location,
                fire_hose_per_floor_count=fire_hose_per_floor_count,
                fire_hose_size=fire_hose_size,
                fire_hose_length=fire_hose_length,
                fire_hose_nozzle=fire_hose_nozzle,
                fire_lane=fire_lane,
                fire_hydrant_location=fire_hydrant_location,
                portable_fire_extinguisher_type=portable_fire_extinguisher_type,
                portable_fire_extinguisher_capacity=portable_fire_extinguisher_capacity,
                portable_fire_extinguisher_count=portable_fire_extinguisher_count,
                portable_fire_extinguisher_with_ps_mark=portable_fire_extinguisher_with_ps_mark,
                portable_fire_extinguisher_with_iso_mark=portable_fire_extinguisher_with_iso_mark,
                portable_fire_extinguisher_maintained=portable_fire_extinguisher_maintained,
                portable_fire_extinguisher_conspicuously_located=portable_fire_extinguisher_conspicuously_located,
                portable_fire_extinguisher_accessible=portable_fire_extinguisher_accessible,
                portable_fire_extinguisher_other_type=portable_fire_extinguisher_other_type,
                sprinkler_system_agent_used=sprinkler_system_agent_used,
                jockey_pump_capacity=jockey_pump_capacity,
                fire_pump_capacity=fire_pump_capacity,
                gpm_tank_capacity=gpm_tank_capacity,
                maintaining_line_pressure=maintaining_line_pressure,
                farthest_sprinkler_head_pressure=farthest_sprinkler_head_pressure,
                riser_size=riser_size,
                type_of_heads_installed=type_of_heads_installed,
                heads_per_floor_count=heads_per_floor_count,
                heads_total_count=heads_total_count,
                spacing_of_heads=spacing_of_heads,
                location_of_fire_dept_connection=location_of_fire_dept_connection,
                plan_submitted=plan_submitted,
                firewall_required=firewall_required,
                firewall_provided=firewall_provided,
                firewall_opening=firewall_opening,
                boiler_provided=boiler_provided,
                boiler_unit_count=boiler_unit_count,
                boiler_fuel=boiler_fuel,
                boiler_capacity=boiler_capacity,
                boiler_container=boiler_container,
                boiler_location=boiler_location,
                lpg_installation_with_permit=lpg_installation_with_permit,
                fuel_with_storage_permit=fuel_with_storage_permit,
                generator_set=generator_set,
                generator_set_type=generator_set_type,
                generator_fuel=generator_fuel,
                generator_capacity=generator_capacity,
                generator_location=generator_location,
                generator_bound_on_wall=generator_bound_on_wall,
                generator_container=generator_container,
                generator_dispensing_system=generator_dispensing_system,
                generator_output_capacity=generator_output_capacity,
                generator_mechanical_permit=generator_mechanical_permit,
                generator_fuel_storage_permit=generator_fuel_storage_permit,
                generator_others=generator_others,
                generator_automatic_transfer_switch=generator_automatic_transfer_switch,
                generator_time_interval=generator_time_interval,
                refuse_handling=refuse_handling,
                refuse_handling_enclosure=refuse_handling_enclosure,
                refuse_handling_fire_protection=refuse_handling_fire_protection,
                electrical_hazard=electrical_hazard,
                electrical_hazard_location=electrical_hazard_location,
                mechanical_hazard=mechanical_hazard,
                mechanical_hazard_location=mechanical_hazard_location,
                elevator_count=elevator_count,
                other_service_system=other_service_system,
                hazardous_area=hazardous_area,
                hazardous_area_other=hazardous_area_other,
                separation_fire_rated=separation_fire_rated,
                type_of_protection=type_of_protection,
                separation_fire_rated_count=separation_fire_rated_count,
                separation_fire_rated_accessible=separation_fire_rated_accessible,
                separation_fire_rated_fuel=separation_fire_rated_fuel,
                separation_fire_rated_location=separation_fire_rated_location,
                separation_fire_rated_permit=separation_fire_rated_permit,
                hazardous_material=hazardous_material,
                hazardous_material_stored=hazardous_material_stored,
                fire_brigade_organization=fire_brigade_organization,
                fire_safety_seminar=fire_safety_seminar,
                employee_trained_in_emergency_procedures=employee_trained_in_emergency_procedures,
                evacuation_drill_first=evacuation_drill_first,
                evacuation_drill_second=evacuation_drill_second,
                defects=defects,
                defects_photo=defects_photo,
                recommendations=recommendations,
                building=building,
                business=business,
                building_permit_date_issued=building_permit_date_issued,
                occupancy_permit_date_issued=occupancy_permit_date_issued,
                fsic_date_issued=fsic_date_issued,
                fire_drill_certificate_date_issued=fire_drill_certificate_date_issued,
                violation_control_no_date_issued=violation_control_no_date_issued,
                electrical_inspection_date_issued=electrical_inspection_date_issued,
                insurance_date_issued=insurance_date_issued,
                main_stair_pressurized_stairway_last_tested=main_stair_pressurized_stairway_last_tested,
                fire_door_pressurized_stairway_last_tested=fire_door_pressurized_stairway_last_tested,
                vertical_opening_last_tested=vertical_opening_last_tested,
                fire_hose_last_tested=fire_hose_last_tested,
                sprinkler_system_last_tested=sprinkler_system_last_tested,
                sprinkler_system_last_conducted=sprinkler_system_last_conducted,
                certificate_of_installation_date=certificate_of_installation_date,
                generator_mechanical_permit_date_issued=generator_mechanical_permit_date_issued,
                date_checked=checked_date
            )

            checklist.save()
            return checklist, 'Checklist recorded!'
        else:
            return False, m
