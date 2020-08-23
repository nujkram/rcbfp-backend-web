from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from buildings.constants import LOCATION_CHOICES, CURRENT_CHOICES
from buildings.models.building.building_models import Building
from business.models import Business

from checklists.models import Checklist as Master
from admin_dashboards.controllers.views.admin_dashboards.checklist.forms import ChecklistForm as MasterForm
from locations.models import Region, City, Province

"""
URLS
# Checklist

from admin_dashboards.controllers.views.admin_dashboards.checklist import main as checklist_views

urlpatterns += {
    path(
        'checklist/list',
        checklist_views.AdminDashboardChecklistListView.as_view(),
        name='admin_dashboard_checklist_list'
    ),
    path(
        'checklist/<pk>/detail',
        checklist_views.AdminDashboardChecklistDetailView.as_view(),
        name='admin_dashboard_checklist_detail'
    ),
    path(
        'checklist/create',
        checklist_views.AdminDashboardChecklistCreateView.as_view(),
        name='admin_dashboard_checklist_create'
    ),
    path(
        'incident/<pk>/update',
        checklist_views.AdminDashboardChecklistUpdateView.as_view(),
        name='admin_dashboard_checklist_update'
    ),
    path(
        'checklist/<pk>/delete',
        checklist_views.AdminDashboardChecklistDeleteView.as_view(),
        name='admin_dashboard_checklist_delete'
    )
}
"""


class AdminDashboardChecklistListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Checklist.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        obj_list = Master.objects.actives()
        paginator = Paginator(obj_list, 1000)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Checklist",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "checklist/list.html", context)


class AdminDashboardChecklistCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Checklist.

    Allowed HTTP verbs:
        - GET
        - POST

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        form = MasterForm
        location_choices = LOCATION_CHOICES
        current_choices = CURRENT_CHOICES

        if 'checklist_formdata' in request.session:
            checklist_formdata = request.session['checklist_formdata']
            del request.session['checklist_formdata']
        else:
            checklist_formdata = {
                'first_name': '',
                'middle_name': '',
                'last_name': '',
                'policy_no': '',
                'building_permit': '',
                'occupancy_permit': '',
                'fsic_control_no': '',
                'fsic_fee': '',
                'fire_drill_certificate': '',
                'violation_control_no': '',
                'electrical_inspection_no': '',
                'sectional_occupancy': '',
                'occupant_load': '',
                'egress_capacity': '',
                'any_renovation': '',
                'renovation_specification': '',
                'horizontal_exit_capacity': '',
                'exit_stair_capacity': '',
                'no_of_exits': '',
                'is_exits_remote': '',
                'exit_location': '',
                'any_enclosure': '',
                'is_exit_accessible': '',
                'is_fire_doors_provided': '',
                'self_closing_mechanism': '',
                'panic_hardware': '',
                'readily_accessible': '',
                'travel_distance_within_limit': '',
                'adequate_illumination': '',
                'panic_hardware_operational': '',
                'doors_open_easily': '',
                'bldg_with_mezzanine': '',
                'is_obstructed': '',
                'dead_ends_within_limits': '',
                'proper_rating_illumination': '',
                'door_swing_in_the_direction_of_exit': '',
                'self_closure_operational': '',
                'mezzanine_with_proper_exits': '',
                'corridors_of_sufficient_size': '',
                'main_stair_width': '',
                'construction': '',
                'main_stair_railings': '',
                'main_stair_railings_built': '',
                'main_stair_any_enclosure_provided': '',
                'enclosure_built': '',
                'any_openings': '',
                'main_stair_door_proper_rating': '',
                'main_stair_door_provided_with_vision_panel': '',
                'main_stair_door_vision_panel_built': '',
                'main_stair_pressurized_stairway': '',
                'main_stair_type_of_pressurized_stairway': '',
                'fire_escape_count': '',
                'fire_escape_width': '',
                'fire_escape_construction': '',
                'fire_escape_railings': '',
                'fire_escape_built': '',
                'fire_escape_location': '',
                'fire_escape_obstruction': '',
                'discharge_of_exits': '',
                'fire_escape_any_enclosure_provided': '',
                'fire_escape_enclosure': '',
                'fire_escape_opening': '',
                'fire_escape_opening_protected': '',
                'fire_door_provided': '',
                'fire_door_width': '',
                'fire_door_construction': '',
                'fire_door_door_proper_rating': '',
                'fire_door_door_provided_with_vision_panel': '',
                'fire_door_door_vision_panel_built': '',
                'fire_door_pressurized_stairway': '',
                'fire_door_type_of_pressurized_stairway': '',
                'horizontal_exit_width': '',
                'horizontal_exit_construction': '',
                'horizontal_exit_vision_panel': '',
                'horizontal_exit_door_swing_in_direction_of_egress': '',
                'horizontal_exit_with_self_closing_device': '',
                'horizontal_exit_corridor_width': '',
                'horizontal_exit_corridor_construction': '',
                'horizontal_exit_corridor_walls_extended': '',
                'horizontal_exit_properly_illuminated': '',
                'horizontal_exit_readily_visible': '',
                'horizontal_exit_properly_marked': '',
                'horizontal_exit_with_illuminated_directional_sign': '',
                'horizontal_exit_properly_located': '',
                'ramps_provided': '',
                'ramps_type': '',
                'ramps_width': '',
                'ramps_class': '',
                'ramps_railing_provided': '',
                'ramps_height': '',
                'ramps_enclosure': '',
                'ramps_construction': '',
                'ramps_fire_doors': '',
                'ramps_fire_doors_width': '',
                'ramps_fire_doors_construction': '',
                'ramps_with_self_closing_device': '',
                'ramps_door_with_proper_rating': '',
                'ramps_door_with_vision_panel': '',
                'ramps_door_vision_panel_built': '',
                'ramps_door_swing_in_direction_of_egress': '',
                'ramps_obstruction': '',
                'ramps_discharge_of_exit': '',
                'safe_refuge_provided': '',
                'safe_refuge_type': '',
                'safe_refuge_enclosure': '',
                'safe_refuge_construction': '',
                'safe_refuge_fire_door': '',
                'safe_refuge_fire_door_width': '',
                'safe_refuge_fire_door_construction': '',
                'safe_refuge_with_self_closing_device': '',
                'safe_refuge_door_proper_rating': '',
                'safe_refuge_with_vision_panel': '',
                'safe_refuge_vision_panel_built': '',
                'safe_refuge_swing_in_direction_of_egress': '',
                'emergency_light': '',
                'emergency_light_source': '',
                'emergency_light_per_floor_count': '',
                'emergency_light_hallway_count': '',
                'emergency_light_stairway_count': '',
                'emergency_light_operational': '',
                'emergency_light_exit_path_properly_illuminated': '',
                'emergency_light_tested_monthly': '',
                'exit_signs_illuminated': '',
                'exit_signs_location': '',
                'exit_signs_source': '',
                'exit_signs_visible': '',
                'exit_signs_min_letter_size': '',
                'exit_route_posted_on_lobby': '',
                'exit_route_posted_on_rooms': '',
                'directional_exit_signs': '',
                'directional_exit_signs_location': '',
                'no_smoking_sign': '',
                'dead_end_sign': '',
                'elevator_sign': '',
                'keep_door_closed_sign': '',
                'others': '',
                'vertical_openings_properly_protected': '',
                'vertical_openings_atrium': '',
                'fire_doors_good_condition': '',
                'elevator_opening_protected': '',
                'pipe_chase_opening_protected': '',
                'aircon_ducts_with_dumper': '',
                'garbage_chute_protected': '',
                'between_floor_protected': '',
                'standpipe_type': '',
                'standpipe_tank_capacity': '',
                'standpipe_location': '',
                'siamese_intake_provided': '',
                'siamese_intake_location': '',
                'siamese_intake_size': '',
                'siamese_intake_count': '',
                'siamese_intake_accessible': '',
                'fire_hose_cabinet': '',
                'fire_hose_cabinet_accessories': '',
                'fire_hose_cabinet_location': '',
                'fire_hose_per_floor_count': '',
                'fire_hose_size': '',
                'fire_hose_length': '',
                'fire_hose_nozzle': '',
                'fire_lane': '',
                'fire_hydrant_location': '',
                'portable_fire_extinguisher_type': '',
                'portable_fire_extinguisher_capacity': '',
                'portable_fire_extinguisher_count': '',
                'portable_fire_extinguisher_with_ps_mark': '',
                'portable_fire_extinguisher_with_iso_mark': '',
                'portable_fire_extinguisher_maintained': '',
                'portable_fire_extinguisher_conspicuously_located': '',
                'portable_fire_extinguisher_accessible': '',
                'portable_fire_extinguisher_other_type': '',
                'sprinkler_system_agent_used': '',
                'jockey_pump_capacity': '',
                'fire_pump_capacity': '',
                'gpm_tank_capacity': '',
                'maintaining_line_pressure': '',
                'farthest_sprinkler_head_pressure': '',
                'riser_size': '',
                'type_of_heads_installed': '',
                'heads_per_floor_count': '',
                'heads_total_count': '',
                'spacing_of_heads': '',
                'location_of_fire_dept_connection': '',
                'plan_submitted': '',
                'firewall_required': '',
                'firewall_provided': '',
                'firewall_opening': '',
                'boiler_provided': '',
                'boiler_unit_count': '',
                'boiler_fuel': '',
                'boiler_capacity': '',
                'boiler_container': '',
                'boiler_location': '',
                'lpg_installation_with_permit': '',
                'fuel_with_storage_permit': '',
                'generator_set': '',
                'generator_set_type': '',
                'generator_fuel': '',
                'generator_capacity': '',
                'generator_location': '',
                'generator_bound_on_wall': '',
                'generator_container': '',
                'generator_dispensing_system': '',
                'generator_output_capacity': '',
                'generator_mechanical_permit': '',
                'generator_fuel_storage_permit': '',
                'generator_others': '',
                'generator_automatic_transfer_switch': '',
                'generator_time_interval': '',
                'refuse_handling': '',
                'refuse_handling_enclosure': '',
                'refuse_handling_fire_protection': '',
                'electrical_hazard': '',
                'electrical_hazard_location': '',
                'mechanical_hazard': '',
                'mechanical_hazard_location': '',
                'elevator_count': '',
                'other_service_system': '',
                'hazardous_area': '',
                'hazardous_area_other': '',
                'separation_fire_rated': '',
                'type_of_protection': '',
                'separation_fire_rated_count': '',
                'separation_fire_rated_capacity': '',
                'separation_fire_rated_accessible': '',
                'separation_fire_rated_fuel': '',
                'separation_fire_rated_location': '',
                'separation_fire_rated_permit': '',
                'hazardous_material': '',
                'hazardous_material_stored': '',
                'fire_brigade_organization': '',
                'fire_safety_seminar': '',
                'employee_trained_in_emergency_procedures': '',
                'evacuation_drill_first': '',
                'evacuation_drill_second': '',
                'defects': '',
                'defects_photo': '',
                'recommendations': '',
                'building': '',
                'business': '',
                'building_permit_date_issued': '',
                'occupancy_permit_date_issued': '',
                'fsic_date_issued': '',
                'fire_drill_certificate_date_issued': '',
                'violation_control_no_date_issued': '',
                'electrical_inspection_date_issued': '',
                'insurance_date_issued': '',
                'main_stair_pressurized_stairway_last_tested': '',
                'fire_door_pressurized_stairway_last_tested': '',
                'vertical_opening_last_tested': '',
                'fire_hose_last_tested': '',
                'sprinkler_system_last_tested': '',
                'sprinkler_system_last_conducted': '',
                'certificate_of_installation_date': '',
                'generator_mechanical_permit_date_issued': '',
                'date_checked': '',
            }

        context = {
            "page_title": "Create new Checklist",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "checklist_formdata": checklist_formdata,
            "form": form,
            "location_choices": location_choices,
            "current_choices": current_choices,
        }

        return render(request, "checklist/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(request.POST, request.FILES)

        checklist_formdata = {
            'first_name': request.post.get('first_name', ''),
            'middle_name': request.post.get('middle_name', ''),
            'last_name': request.post.get('last_name', ''),
            'policy_no': request.post.get('policy_no', ''),
            'building_permit': request.post.get('building_permit', ''),
            'occupancy_permit': request.post.get('occupancy_permit', ''),
            'fsic_control_no': request.post.get('fsic_control_no', ''),
            'fsic_fee': request.post.get('fsic_fee', ''),
            'fire_drill_certificate': request.post.get('fire_drill_certificate', ''),
            'violation_control_no': request.post.get('violation_control_no', ''),
            'electrical_inspection_no': request.post.get('electrical_inspection_no', ''),
            'sectional_occupancy': request.post.get('sectional_occupancy', ''),
            'occupant_load': request.post.get('occupant_load', ''),
            'egress_capacity': request.post.get('egress_capacity', ''),
            'any_renovation': request.post.get('any_renovation', ''),
            'renovation_specification': request.post.get('renovation_specification', ''),
            'horizontal_exit_capacity': request.post.get('horizontal_exit_capacity', ''),
            'exit_stair_capacity': request.post.get('exit_stair_capacity', ''),
            'no_of_exits': request.post.get('no_of_exits', ''),
            'is_exits_remote': request.post.get('is_exits_remote', ''),
            'exit_location': request.post.get('exit_location', ''),
            'any_enclosure': request.post.get('any_enclosure', ''),
            'is_exit_accessible': request.post.get('is_exit_accessible', ''),
            'is_fire_doors_provided': request.post.get('is_fire_doors_provided', ''),
            'self_closing_mechanism': request.post.get('self_closing_mechanism', ''),
            'panic_hardware': request.post.get('panic_hardware', ''),
            'readily_accessible': request.post.get('readily_accessible', ''),
            'travel_distance_within_limit': request.post.get('travel_distance_within_limit', ''),
            'adequate_illumination': request.post.get('adequate_illumination', ''),
            'panic_hardware_operational': request.post.get('panic_hardware_operational', ''),
            'doors_open_easily': request.post.get('doors_open_easily', ''),
            'bldg_with_mezzanine': request.post.get('bldg_with_mezzanine', ''),
            'is_obstructed': request.post.get('is_obstructed', ''),
            'dead_ends_within_limits': request.post.get('dead_ends_within_limits', ''),
            'proper_rating_illumination': request.post.get('proper_rating_illumination', ''),
            'door_swing_in_the_direction_of_exit': request.post.get('door_swing_in_the_direction_of_exit', ''),
            'self_closure_operational': request.post.get('self_closure_operational', ''),
            'mezzanine_with_proper_exits': request.post.get('mezzanine_with_proper_exits', ''),
            'corridors_of_sufficient_size': request.post.get('corridors_of_sufficient_size', ''),
            'main_stair_width': request.post.get('main_stair_width', ''),
            'construction': request.post.get('construction', ''),
            'main_stair_railings': request.post.get('main_stair_railings', ''),
            'main_stair_railings_built': request.post.get('main_stair_railings_built', ''),
            'main_stair_any_enclosure_provided': request.post.get('main_stair_any_enclosure_provided', ''),
            'enclosure_built': request.post.get('enclosure_built', ''),
            'any_openings': request.post.get('any_openings', ''),
            'main_stair_door_proper_rating': request.post.get('main_stair_door_proper_rating', ''),
            'main_stair_door_provided_with_vision_panel': request.post.get('main_stair_door_provided_with_vision_panel',
                                                                           ''),
            'main_stair_door_vision_panel_built': request.post.get('main_stair_door_vision_panel_built', ''),
            'main_stair_pressurized_stairway': request.post.get('main_stair_pressurized_stairway', ''),
            'main_stair_type_of_pressurized_stairway': request.post.get('main_stair_type_of_pressurized_stairway', ''),
            'fire_escape_count': request.post.get('fire_escape_count', ''),
            'fire_escape_width': request.post.get('fire_escape_width', ''),
            'fire_escape_construction': request.post.get('fire_escape_construction', ''),
            'fire_escape_railings': request.post.get('fire_escape_railings', ''),
            'fire_escape_built': request.post.get('fire_escape_built', ''),
            'fire_escape_location': request.post.get('fire_escape_location', ''),
            'fire_escape_obstruction': request.post.get('fire_escape_obstruction', ''),
            'discharge_of_exits': request.post.get('discharge_of_exits', ''),
            'fire_escape_any_enclosure_provided': request.post.get('fire_escape_any_enclosure_provided', ''),
            'fire_escape_enclosure': request.post.get('fire_escape_enclosure', ''),
            'fire_escape_opening': request.post.get('fire_escape_opening', ''),
            'fire_escape_opening_protected': request.post.get('fire_escape_opening_protected', ''),
            'fire_door_provided': request.post.get('fire_door_provided', ''),
            'fire_door_width': request.post.get('fire_door_width', ''),
            'fire_door_construction': request.post.get('fire_door_construction', ''),
            'fire_door_door_proper_rating': request.post.get('fire_door_door_proper_rating', ''),
            'fire_door_door_provided_with_vision_panel': request.post.get('fire_door_door_provided_with_vision_panel',
                                                                          ''),
            'fire_door_door_vision_panel_built': request.post.get('fire_door_door_vision_panel_built', ''),
            'fire_door_pressurized_stairway': request.post.get('fire_door_pressurized_stairway', ''),
            'fire_door_type_of_pressurized_stairway': request.post.get('fire_door_type_of_pressurized_stairway', ''),
            'horizontal_exit_width': request.post.get('horizontal_exit_width', ''),
            'horizontal_exit_construction': request.post.get('horizontal_exit_construction', ''),
            'horizontal_exit_vision_panel': request.post.get('horizontal_exit_vision_panel', ''),
            'horizontal_exit_door_swing_in_direction_of_egress': request.post.get(
                'horizontal_exit_door_swing_in_direction_of_egress', ''),
            'horizontal_exit_with_self_closing_device': request.post.get('horizontal_exit_with_self_closing_device',
                                                                         ''),
            'horizontal_exit_corridor_width': request.post.get('horizontal_exit_corridor_width', ''),
            'horizontal_exit_corridor_construction': request.post.get('horizontal_exit_corridor_construction', ''),
            'horizontal_exit_corridor_walls_extended': request.post.get('horizontal_exit_corridor_walls_extended', ''),
            'horizontal_exit_properly_illuminated': request.post.get('horizontal_exit_properly_illuminated', ''),
            'horizontal_exit_readily_visible': request.post.get('horizontal_exit_readily_visible', ''),
            'horizontal_exit_properly_marked': request.post.get('horizontal_exit_properly_marked', ''),
            'horizontal_exit_with_illuminated_directional_sign': request.post.get(
                'horizontal_exit_with_illuminated_directional_sign', ''),
            'horizontal_exit_properly_located': request.post.get('horizontal_exit_properly_located', ''),
            'ramps_provided': request.post.get('ramps_provided', ''),
            'ramps_type': request.post.get('ramps_type', ''),
            'ramps_width': request.post.get('ramps_width', ''),
            'ramps_class': request.post.get('ramps_class', ''),
            'ramps_railing_provided': request.post.get('ramps_railing_provided', ''),
            'ramps_height': request.post.get('ramps_height', ''),
            'ramps_enclosure': request.post.get('ramps_enclosure', ''),
            'ramps_construction': request.post.get('ramps_construction', ''),
            'ramps_fire_doors': request.post.get('ramps_fire_doors', ''),
            'ramps_fire_doors_width': request.post.get('ramps_fire_doors_width', ''),
            'ramps_fire_doors_construction': request.post.get('ramps_fire_doors_construction', ''),
            'ramps_with_self_closing_device': request.post.get('ramps_with_self_closing_device', ''),
            'ramps_door_with_proper_rating': request.post.get('ramps_door_with_proper_rating', ''),
            'ramps_door_with_vision_panel': request.post.get('ramps_door_with_vision_panel', ''),
            'ramps_door_vision_panel_built': request.post.get('ramps_door_vision_panel_built', ''),
            'ramps_door_swing_in_direction_of_egress': request.post.get('ramps_door_swing_in_direction_of_egress', ''),
            'ramps_obstruction': request.post.get('ramps_obstruction', ''),
            'ramps_discharge_of_exit': request.post.get('ramps_discharge_of_exit', ''),
            'safe_refuge_provided': request.post.get('safe_refuge_provided', ''),
            'safe_refuge_type': request.post.get('safe_refuge_type', ''),
            'safe_refuge_enclosure': request.post.get('safe_refuge_enclosure', ''),
            'safe_refuge_construction': request.post.get('safe_refuge_construction', ''),
            'safe_refuge_fire_door': request.post.get('safe_refuge_fire_door', ''),
            'safe_refuge_fire_door_width': request.post.get('safe_refuge_fire_door_width', ''),
            'safe_refuge_fire_door_construction': request.post.get('safe_refuge_fire_door_construction', ''),
            'safe_refuge_with_self_closing_device': request.post.get('safe_refuge_with_self_closing_device', ''),
            'safe_refuge_door_proper_rating': request.post.get('safe_refuge_door_proper_rating', ''),
            'safe_refuge_with_vision_panel': request.post.get('safe_refuge_with_vision_panel', ''),
            'safe_refuge_vision_panel_built': request.post.get('safe_refuge_vision_panel_built', ''),
            'safe_refuge_swing_in_direction_of_egress': request.post.get('safe_refuge_swing_in_direction_of_egress',
                                                                         ''),
            'emergency_light': request.post.get('emergency_light', ''),
            'emergency_light_source': request.post.get('emergency_light_source', ''),
            'emergency_light_per_floor_count': request.post.get('emergency_light_per_floor_count', ''),
            'emergency_light_hallway_count': request.post.get('emergency_light_hallway_count', ''),
            'emergency_light_stairway_count': request.post.get('emergency_light_stairway_count', ''),
            'emergency_light_operational': request.post.get('emergency_light_operational', ''),
            'emergency_light_exit_path_properly_illuminated': request.post.get(
                'emergency_light_exit_path_properly_illuminated', ''),
            'emergency_light_tested_monthly': request.post.get('emergency_light_tested_monthly', ''),
            'exit_signs_illuminated': request.post.get('exit_signs_illuminated', ''),
            'exit_signs_location': request.post.get('exit_signs_location', ''),
            'exit_signs_source': request.post.get('exit_signs_source', ''),
            'exit_signs_visible': request.post.get('exit_signs_visible', ''),
            'exit_signs_min_letter_size': request.post.get('exit_signs_min_letter_size', ''),
            'exit_route_posted_on_lobby': request.post.get('exit_route_posted_on_lobby', ''),
            'exit_route_posted_on_rooms': request.post.get('exit_route_posted_on_rooms', ''),
            'directional_exit_signs': request.post.get('directional_exit_signs', ''),
            'directional_exit_signs_location': request.post.get('directional_exit_signs_location', ''),
            'no_smoking_sign': request.post.get('no_smoking_sign', ''),
            'dead_end_sign': request.post.get('dead_end_sign', ''),
            'elevator_sign': request.post.get('elevator_sign', ''),
            'keep_door_closed_sign': request.post.get('keep_door_closed_sign', ''),
            'others': request.post.get('others', ''),
            'vertical_openings_properly_protected': request.post.get('vertical_openings_properly_protected', ''),
            'vertical_openings_atrium': request.post.get('vertical_openings_atrium', ''),
            'fire_doors_good_condition': request.post.get('fire_doors_good_condition', ''),
            'elevator_opening_protected': request.post.get('elevator_opening_protected', ''),
            'pipe_chase_opening_protected': request.post.get('pipe_chase_opening_protected', ''),
            'aircon_ducts_with_dumper': request.post.get('aircon_ducts_with_dumper', ''),
            'garbage_chute_protected': request.post.get('garbage_chute_protected', ''),
            'between_floor_protected': request.post.get('between_floor_protected', ''),
            'standpipe_type': request.post.get('standpipe_type', ''),
            'standpipe_tank_capacity': request.post.get('standpipe_tank_capacity', ''),
            'standpipe_location': request.post.get('standpipe_location', ''),
            'siamese_intake_provided': request.post.get('siamese_intake_provided', ''),
            'siamese_intake_location': request.post.get('siamese_intake_location', ''),
            'siamese_intake_size': request.post.get('siamese_intake_size', ''),
            'siamese_intake_count': request.post.get('siamese_intake_count', ''),
            'siamese_intake_accessible': request.post.get('siamese_intake_accessible', ''),
            'fire_hose_cabinet': request.post.get('fire_hose_cabinet', ''),
            'fire_hose_cabinet_accessories': request.post.get('fire_hose_cabinet_accessories', ''),
            'fire_hose_cabinet_location': request.post.get('fire_hose_cabinet_location', ''),
            'fire_hose_per_floor_count': request.post.get('fire_hose_per_floor_count', ''),
            'fire_hose_size': request.post.get('fire_hose_size', ''),
            'fire_hose_length': request.post.get('fire_hose_length', ''),
            'fire_hose_nozzle': request.post.get('fire_hose_nozzle', ''),
            'fire_lane': request.post.get('fire_lane', ''),
            'fire_hydrant_location': request.post.get('fire_hydrant_location', ''),
            'portable_fire_extinguisher_type': request.post.get('portable_fire_extinguisher_type', ''),
            'portable_fire_extinguisher_capacity': request.post.get('portable_fire_extinguisher_capacity', ''),
            'portable_fire_extinguisher_count': request.post.get('portable_fire_extinguisher_count', ''),
            'portable_fire_extinguisher_with_ps_mark': request.post.get('portable_fire_extinguisher_with_ps_mark', ''),
            'portable_fire_extinguisher_with_iso_mark': request.post.get('portable_fire_extinguisher_with_iso_mark',
                                                                         ''),
            'portable_fire_extinguisher_maintained': request.post.get('portable_fire_extinguisher_maintained', ''),
            'portable_fire_extinguisher_conspicuously_located': request.post.get(
                'portable_fire_extinguisher_conspicuously_located', ''),
            'portable_fire_extinguisher_accessible': request.post.get('portable_fire_extinguisher_accessible', ''),
            'portable_fire_extinguisher_other_type': request.post.get('portable_fire_extinguisher_other_type', ''),
            'sprinkler_system_agent_used': request.post.get('sprinkler_system_agent_used', ''),
            'jockey_pump_capacity': request.post.get('jockey_pump_capacity', ''),
            'fire_pump_capacity': request.post.get('fire_pump_capacity', ''),
            'gpm_tank_capacity': request.post.get('gpm_tank_capacity', ''),
            'maintaining_line_pressure': request.post.get('maintaining_line_pressure', ''),
            'farthest_sprinkler_head_pressure': request.post.get('farthest_sprinkler_head_pressure', ''),
            'riser_size': request.post.get('riser_size', ''),
            'type_of_heads_installed': request.post.get('type_of_heads_installed', ''),
            'heads_per_floor_count': request.post.get('heads_per_floor_count', ''),
            'heads_total_count': request.post.get('heads_total_count', ''),
            'spacing_of_heads': request.post.get('spacing_of_heads', ''),
            'location_of_fire_dept_connection': request.post.get('location_of_fire_dept_connection', ''),
            'plan_submitted': request.post.get('plan_submitted', ''),
            'firewall_required': request.post.get('firewall_required', ''),
            'firewall_provided': request.post.get('firewall_provided', ''),
            'firewall_opening': request.post.get('firewall_opening', ''),
            'boiler_provided': request.post.get('boiler_provided', ''),
            'boiler_unit_count': request.post.get('boiler_unit_count', ''),
            'boiler_fuel': request.post.get('boiler_fuel', ''),
            'boiler_capacity': request.post.get('boiler_capacity', ''),
            'boiler_container': request.post.get('boiler_container', ''),
            'boiler_location': request.post.get('boiler_location', ''),
            'lpg_installation_with_permit': request.post.get('lpg_installation_with_permit', ''),
            'fuel_with_storage_permit': request.post.get('fuel_with_storage_permit', ''),
            'generator_set': request.post.get('generator_set', ''),
            'generator_set_type': request.post.get('generator_set_type', ''),
            'generator_fuel': request.post.get('generator_fuel', ''),
            'generator_capacity': request.post.get('generator_capacity', ''),
            'generator_location': request.post.get('generator_location', ''),
            'generator_bound_on_wall': request.post.get('generator_bound_on_wall', ''),
            'generator_container': request.post.get('generator_container', ''),
            'generator_dispensing_system': request.post.get('generator_dispensing_system', ''),
            'generator_output_capacity': request.post.get('generator_output_capacity', ''),
            'generator_mechanical_permit': request.post.get('generator_mechanical_permit', ''),
            'generator_fuel_storage_permit': request.post.get('generator_fuel_storage_permit', ''),
            'generator_others': request.post.get('generator_others', ''),
            'generator_automatic_transfer_switch': request.post.get('generator_automatic_transfer_switch', ''),
            'generator_time_interval': request.post.get('generator_time_interval', ''),
            'refuse_handling': request.post.get('refuse_handling', ''),
            'refuse_handling_enclosure': request.post.get('refuse_handling_enclosure', ''),
            'refuse_handling_fire_protection': request.post.get('refuse_handling_fire_protection', ''),
            'electrical_hazard': request.post.get('electrical_hazard', ''),
            'electrical_hazard_location': request.post.get('electrical_hazard_location', ''),
            'mechanical_hazard': request.post.get('mechanical_hazard', ''),
            'mechanical_hazard_location': request.post.get('mechanical_hazard_location', ''),
            'elevator_count': request.post.get('elevator_count', ''),
            'other_service_system': request.post.get('other_service_system', ''),
            'hazardous_area': request.post.get('hazardous_area', ''),
            'hazardous_area_other': request.post.get('hazardous_area_other', ''),
            'separation_fire_rated': request.post.get('separation_fire_rated', ''),
            'type_of_protection': request.post.get('type_of_protection', ''),
            'separation_fire_rated_count': request.post.get('separation_fire_rated_count', ''),
            'separation_fire_rated_capacity': request.post.get('separation_fire_rated_capacity', ''),
            'separation_fire_rated_accessible': request.post.get('separation_fire_rated_accessible', ''),
            'separation_fire_rated_fuel': request.post.get('separation_fire_rated_fuel', ''),
            'separation_fire_rated_location': request.post.get('separation_fire_rated_location', ''),
            'separation_fire_rated_permit': request.post.get('separation_fire_rated_permit', ''),
            'hazardous_material': request.post.get('hazardous_material', ''),
            'hazardous_material_stored': request.post.get('hazardous_material_stored', ''),
            'fire_brigade_organization': request.post.get('fire_brigade_organization', ''),
            'fire_safety_seminar': request.post.get('fire_safety_seminar', ''),
            'employee_trained_in_emergency_procedures': request.post.get('employee_trained_in_emergency_procedures',
                                                                         ''),
            'evacuation_drill_first': request.post.get('evacuation_drill_first', ''),
            'evacuation_drill_second': request.post.get('evacuation_drill_second', ''),
            'defects': request.post.get('defects', ''),
            'defects_photo': request.post.get('defects_photo', ''),
            'recommendations': request.post.get('recommendations', ''),
            'building': request.post.get('building', ''),
            'business': request.post.get('business', ''),
            'building_permit_date_issued': request.post.get('building_permit_date_issued', ''),
            'occupancy_permit_date_issued': request.post.get('occupancy_permit_date_issued', ''),
            'fsic_date_issued': request.post.get('fsic_date_issued', ''),
            'fire_drill_certificate_date_issued': request.post.get('fire_drill_certificate_date_issued', ''),
            'violation_control_no_date_issued': request.post.get('violation_control_no_date_issued', ''),
            'electrical_inspection_date_issued': request.post.get('electrical_inspection_date_issued', ''),
            'insurance_date_issued': request.post.get('insurance_date_issued', ''),
            'main_stair_pressurized_stairway_last_tested': request.post.get(
                'main_stair_pressurized_stairway_last_tested', ''),
            'fire_door_pressurized_stairway_last_tested': request.post.get('fire_door_pressurized_stairway_last_tested',
                                                                           ''),
            'vertical_opening_last_tested': request.post.get('vertical_opening_last_tested', ''),
            'fire_hose_last_tested': request.post.get('fire_hose_last_tested', ''),
            'sprinkler_system_last_tested': request.post.get('sprinkler_system_last_tested', ''),
            'sprinkler_system_last_conducted': request.post.get('sprinkler_system_last_conducted', ''),
            'certificate_of_installation_date': request.post.get('certificate_of_installation_date', ''),
            'generator_mechanical_permit_date_issued': request.post.get('generator_mechanical_permit_date_issued', ''),
            'date_checked': request.post.get('date_checked', ''),
        }

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']
            policy_no = form.cleaned_data['policy_no']
            building_permit = form.cleaned_data['building_permit']
            occupancy_permit = form.cleaned_data['occupancy_permit']
            fsic_control_no = form.cleaned_data['fsic_control_no']
            fsic_fee = form.cleaned_data['fsic_fee']
            fire_drill_certificate = form.cleaned_data['fire_drill_certificate']
            violation_control_no = form.cleaned_data['violation_control_no']
            electrical_inspection_no = form.cleaned_data['electrical_inspection_no']
            sectional_occupancy = form.cleaned_data['sectional_occupancy']
            occupant_load = form.cleaned_data['occupant_load']
            egress_capacity = form.cleaned_data['egress_capacity']
            any_renovation = form.cleaned_data['any_renovation']
            renovation_specification = form.cleaned_data['renovation_specification']
            horizontal_exit_capacity = form.cleaned_data['horizontal_exit_capacity']
            exit_stair_capacity = form.cleaned_data['exit_stair_capacity']
            no_of_exits = form.cleaned_data['no_of_exits']
            is_exits_remote = form.cleaned_data['is_exits_remote']
            exit_location = form.cleaned_data['exit_location']
            any_enclosure = form.cleaned_data['any_enclosure']
            is_exit_accessible = form.cleaned_data['is_exit_accessible']
            is_fire_doors_provided = form.cleaned_data['is_fire_doors_provided']
            self_closing_mechanism = form.cleaned_data['self_closing_mechanism']
            panic_hardware = form.cleaned_data['panic_hardware']
            readily_accessible = form.cleaned_data['readily_accessible']
            travel_distance_within_limit = form.cleaned_data['travel_distance_within_limit']
            adequate_illumination = form.cleaned_data['adequate_illumination']
            panic_hardware_operational = form.cleaned_data['panic_hardware_operational']
            doors_open_easily = form.cleaned_data['doors_open_easily']
            bldg_with_mezzanine = form.cleaned_data['bldg_with_mezzanine']
            is_obstructed = form.cleaned_data['is_obstructed']
            dead_ends_within_limits = form.cleaned_data['dead_ends_within_limits']
            proper_rating_illumination = form.cleaned_data['proper_rating_illumination']
            door_swing_in_the_direction_of_exit = form.cleaned_data['door_swing_in_the_direction_of_exit']
            self_closure_operational = form.cleaned_data['self_closure_operational']
            mezzanine_with_proper_exits = form.cleaned_data['mezzanine_with_proper_exits']
            corridors_of_sufficient_size = form.cleaned_data['corridors_of_sufficient_size']
            main_stair_width = form.cleaned_data['main_stair_width']
            construction = form.cleaned_data['construction']
            main_stair_railings = form.cleaned_data['main_stair_railings']
            main_stair_railings_built = form.cleaned_data['main_stair_railings_built']
            main_stair_any_enclosure_provided = form.cleaned_data['main_stair_any_enclosure_provided']
            enclosure_built = form.cleaned_data['enclosure_built']
            any_openings = form.cleaned_data['any_openings']
            main_stair_door_proper_rating = form.cleaned_data['main_stair_door_proper_rating']
            main_stair_door_provided_with_vision_panel = form.cleaned_data['main_stair_door_provided_with_vision_panel']
            main_stair_door_vision_panel_built = form.cleaned_data['main_stair_door_vision_panel_built']
            main_stair_pressurized_stairway = form.cleaned_data['main_stair_pressurized_stairway']
            main_stair_type_of_pressurized_stairway = form.cleaned_data['main_stair_type_of_pressurized_stairway']
            fire_escape_count = form.cleaned_data['fire_escape_count']
            fire_escape_width = form.cleaned_data['fire_escape_width']
            fire_escape_construction = form.cleaned_data['fire_escape_construction']
            fire_escape_railings = form.cleaned_data['fire_escape_railings']
            fire_escape_built = form.cleaned_data['fire_escape_built']
            fire_escape_location = form.cleaned_data['fire_escape_location']
            fire_escape_obstruction = form.cleaned_data['fire_escape_obstruction']
            discharge_of_exits = form.cleaned_data['discharge_of_exits']
            fire_escape_any_enclosure_provided = form.cleaned_data['fire_escape_any_enclosure_provided']
            fire_escape_enclosure = form.cleaned_data['fire_escape_enclosure']
            fire_escape_opening = form.cleaned_data['fire_escape_opening']
            fire_escape_opening_protected = form.cleaned_data['fire_escape_opening_protected']
            fire_door_provided = form.cleaned_data['fire_door_provided']
            fire_door_width = form.cleaned_data['fire_door_width']
            fire_door_construction = form.cleaned_data['fire_door_construction']
            fire_door_door_proper_rating = form.cleaned_data['fire_door_door_proper_rating']
            fire_door_door_provided_with_vision_panel = form.cleaned_data['fire_door_door_provided_with_vision_panel']
            fire_door_door_vision_panel_built = form.cleaned_data['fire_door_door_vision_panel_built']
            fire_door_pressurized_stairway = form.cleaned_data['fire_door_pressurized_stairway']
            fire_door_type_of_pressurized_stairway = form.cleaned_data['fire_door_type_of_pressurized_stairway']
            horizontal_exit_width = form.cleaned_data['horizontal_exit_width']
            horizontal_exit_construction = form.cleaned_data['horizontal_exit_construction']
            horizontal_exit_vision_panel = form.cleaned_data['horizontal_exit_vision_panel']
            horizontal_exit_door_swing_in_direction_of_egress = form.cleaned_data[
                'horizontal_exit_door_swing_in_direction_of_egress']
            horizontal_exit_with_self_closing_device = form.cleaned_data['horizontal_exit_with_self_closing_device']
            horizontal_exit_corridor_width = form.cleaned_data['horizontal_exit_corridor_width']
            horizontal_exit_corridor_construction = form.cleaned_data['horizontal_exit_corridor_construction']
            horizontal_exit_corridor_walls_extended = form.cleaned_data['horizontal_exit_corridor_walls_extended']
            horizontal_exit_properly_illuminated = form.cleaned_data['horizontal_exit_properly_illuminated']
            horizontal_exit_readily_visible = form.cleaned_data['horizontal_exit_readily_visible']
            horizontal_exit_properly_marked = form.cleaned_data['horizontal_exit_properly_marked']
            horizontal_exit_with_illuminated_directional_sign = form.cleaned_data[
                'horizontal_exit_with_illuminated_directional_sign']
            horizontal_exit_properly_located = form.cleaned_data['horizontal_exit_properly_located']
            ramps_provided = form.cleaned_data['ramps_provided']
            ramps_type = form.cleaned_data['ramps_type']
            ramps_width = form.cleaned_data['ramps_width']
            ramps_class = form.cleaned_data['ramps_class']
            ramps_railing_provided = form.cleaned_data['ramps_railing_provided']
            ramps_height = form.cleaned_data['ramps_height']
            ramps_enclosure = form.cleaned_data['ramps_enclosure']
            ramps_construction = form.cleaned_data['ramps_construction']
            ramps_fire_doors = form.cleaned_data['ramps_fire_doors']
            ramps_fire_doors_width = form.cleaned_data['ramps_fire_doors_width']
            ramps_fire_doors_construction = form.cleaned_data['ramps_fire_doors_construction']
            ramps_with_self_closing_device = form.cleaned_data['ramps_with_self_closing_device']
            ramps_door_with_proper_rating = form.cleaned_data['ramps_door_with_proper_rating']
            ramps_door_with_vision_panel = form.cleaned_data['ramps_door_with_vision_panel']
            ramps_door_vision_panel_built = form.cleaned_data['ramps_door_vision_panel_built']
            ramps_door_swing_in_direction_of_egress = form.cleaned_data['ramps_door_swing_in_direction_of_egress']
            ramps_obstruction = form.cleaned_data['ramps_obstruction']
            ramps_discharge_of_exit = form.cleaned_data['ramps_discharge_of_exit']
            safe_refuge_provided = form.cleaned_data['safe_refuge_provided']
            safe_refuge_type = form.cleaned_data['safe_refuge_type']
            safe_refuge_enclosure = form.cleaned_data['safe_refuge_enclosure']
            safe_refuge_construction = form.cleaned_data['safe_refuge_construction']
            safe_refuge_fire_door = form.cleaned_data['safe_refuge_fire_door']
            safe_refuge_fire_door_width = form.cleaned_data['safe_refuge_fire_door_width']
            safe_refuge_fire_door_construction = form.cleaned_data['safe_refuge_fire_door_construction']
            safe_refuge_with_self_closing_device = form.cleaned_data['safe_refuge_with_self_closing_device']
            safe_refuge_door_proper_rating = form.cleaned_data['safe_refuge_door_proper_rating']
            safe_refuge_with_vision_panel = form.cleaned_data['safe_refuge_with_vision_panel']
            safe_refuge_vision_panel_built = form.cleaned_data['safe_refuge_vision_panel_built']
            safe_refuge_swing_in_direction_of_egress = form.cleaned_data['safe_refuge_swing_in_direction_of_egress']
            emergency_light = form.cleaned_data['emergency_light']
            emergency_light_source = form.cleaned_data['emergency_light_source']
            emergency_light_per_floor_count = form.cleaned_data['emergency_light_per_floor_count']
            emergency_light_hallway_count = form.cleaned_data['emergency_light_hallway_count']
            emergency_light_stairway_count = form.cleaned_data['emergency_light_stairway_count']
            emergency_light_operational = form.cleaned_data['emergency_light_operational']
            emergency_light_exit_path_properly_illuminated = form.cleaned_data[
                'emergency_light_exit_path_properly_illuminated']
            emergency_light_tested_monthly = form.cleaned_data['emergency_light_tested_monthly']
            exit_signs_illuminated = form.cleaned_data['exit_signs_illuminated']
            exit_signs_location = form.cleaned_data['exit_signs_location']
            exit_signs_source = form.cleaned_data['exit_signs_source']
            exit_signs_visible = form.cleaned_data['exit_signs_visible']
            exit_signs_min_letter_size = form.cleaned_data['exit_signs_min_letter_size']
            exit_route_posted_on_lobby = form.cleaned_data['exit_route_posted_on_lobby']
            exit_route_posted_on_rooms = form.cleaned_data['exit_route_posted_on_rooms']
            directional_exit_signs = form.cleaned_data['directional_exit_signs']
            directional_exit_signs_location = form.cleaned_data['directional_exit_signs_location']
            no_smoking_sign = form.cleaned_data['no_smoking_sign']
            dead_end_sign = form.cleaned_data['dead_end_sign']
            elevator_sign = form.cleaned_data['elevator_sign']
            keep_door_closed_sign = form.cleaned_data['keep_door_closed_sign']
            others = form.cleaned_data['others']
            vertical_openings_properly_protected = form.cleaned_data['vertical_openings_properly_protected']
            vertical_openings_atrium = form.cleaned_data['vertical_openings_atrium']
            fire_doors_good_condition = form.cleaned_data['fire_doors_good_condition']
            elevator_opening_protected = form.cleaned_data['elevator_opening_protected']
            pipe_chase_opening_protected = form.cleaned_data['pipe_chase_opening_protected']
            aircon_ducts_with_dumper = form.cleaned_data['aircon_ducts_with_dumper']
            garbage_chute_protected = form.cleaned_data['garbage_chute_protected']
            between_floor_protected = form.cleaned_data['between_floor_protected']
            standpipe_type = form.cleaned_data['standpipe_type']
            standpipe_tank_capacity = form.cleaned_data['standpipe_tank_capacity']
            standpipe_location = form.cleaned_data['standpipe_location']
            siamese_intake_provided = form.cleaned_data['siamese_intake_provided']
            siamese_intake_location = form.cleaned_data['siamese_intake_location']
            siamese_intake_size = form.cleaned_data['siamese_intake_size']
            siamese_intake_count = form.cleaned_data['siamese_intake_count']
            siamese_intake_accessible = form.cleaned_data['siamese_intake_accessible']
            fire_hose_cabinet = form.cleaned_data['fire_hose_cabinet']
            fire_hose_cabinet_accessories = form.cleaned_data['fire_hose_cabinet_accessories']
            fire_hose_cabinet_location = form.cleaned_data['fire_hose_cabinet_location']
            fire_hose_per_floor_count = form.cleaned_data['fire_hose_per_floor_count']
            fire_hose_size = form.cleaned_data['fire_hose_size']
            fire_hose_length = form.cleaned_data['fire_hose_length']
            fire_hose_nozzle = form.cleaned_data['fire_hose_nozzle']
            fire_lane = form.cleaned_data['fire_lane']
            fire_hydrant_location = form.cleaned_data['fire_hydrant_location']
            portable_fire_extinguisher_type = form.cleaned_data['portable_fire_extinguisher_type']
            portable_fire_extinguisher_capacity = form.cleaned_data['portable_fire_extinguisher_capacity']
            portable_fire_extinguisher_count = form.cleaned_data['portable_fire_extinguisher_count']
            portable_fire_extinguisher_with_ps_mark = form.cleaned_data['portable_fire_extinguisher_with_ps_mark']
            portable_fire_extinguisher_with_iso_mark = form.cleaned_data['portable_fire_extinguisher_with_iso_mark']
            portable_fire_extinguisher_maintained = form.cleaned_data['portable_fire_extinguisher_maintained']
            portable_fire_extinguisher_conspicuously_located = form.cleaned_data[
                'portable_fire_extinguisher_conspicuously_located']
            portable_fire_extinguisher_accessible = form.cleaned_data['portable_fire_extinguisher_accessible']
            portable_fire_extinguisher_other_type = form.cleaned_data['portable_fire_extinguisher_other_type']
            sprinkler_system_agent_used = form.cleaned_data['sprinkler_system_agent_used']
            jockey_pump_capacity = form.cleaned_data['jockey_pump_capacity']
            fire_pump_capacity = form.cleaned_data['fire_pump_capacity']
            gpm_tank_capacity = form.cleaned_data['gpm_tank_capacity']
            maintaining_line_pressure = form.cleaned_data['maintaining_line_pressure']
            farthest_sprinkler_head_pressure = form.cleaned_data['farthest_sprinkler_head_pressure']
            riser_size = form.cleaned_data['riser_size']
            type_of_heads_installed = form.cleaned_data['type_of_heads_installed']
            heads_per_floor_count = form.cleaned_data['heads_per_floor_count']
            heads_total_count = form.cleaned_data['heads_total_count']
            spacing_of_heads = form.cleaned_data['spacing_of_heads']
            location_of_fire_dept_connection = form.cleaned_data['location_of_fire_dept_connection']
            plan_submitted = form.cleaned_data['plan_submitted']
            firewall_required = form.cleaned_data['firewall_required']
            firewall_provided = form.cleaned_data['firewall_provided']
            firewall_opening = form.cleaned_data['firewall_opening']
            boiler_provided = form.cleaned_data['boiler_provided']
            boiler_unit_count = form.cleaned_data['boiler_unit_count']
            boiler_fuel = form.cleaned_data['boiler_fuel']
            boiler_capacity = form.cleaned_data['boiler_capacity']
            boiler_container = form.cleaned_data['boiler_container']
            boiler_location = form.cleaned_data['boiler_location']
            lpg_installation_with_permit = form.cleaned_data['lpg_installation_with_permit']
            fuel_with_storage_permit = form.cleaned_data['fuel_with_storage_permit']
            generator_set = form.cleaned_data['generator_set']
            generator_set_type = form.cleaned_data['generator_set_type']
            generator_fuel = form.cleaned_data['generator_fuel']
            generator_capacity = form.cleaned_data['generator_capacity']
            generator_location = form.cleaned_data['generator_location']
            generator_bound_on_wall = form.cleaned_data['generator_bound_on_wall']
            generator_container = form.cleaned_data['generator_container']
            generator_dispensing_system = form.cleaned_data['generator_dispensing_system']
            generator_output_capacity = form.cleaned_data['generator_output_capacity']
            generator_mechanical_permit = form.cleaned_data['generator_mechanical_permit']
            generator_fuel_storage_permit = form.cleaned_data['generator_fuel_storage_permit']
            generator_others = form.cleaned_data['generator_others']
            generator_automatic_transfer_switch = form.cleaned_data['generator_automatic_transfer_switch']
            generator_time_interval = form.cleaned_data['generator_time_interval']
            refuse_handling = form.cleaned_data['refuse_handling']
            refuse_handling_enclosure = form.cleaned_data['refuse_handling_enclosure']
            refuse_handling_fire_protection = form.cleaned_data['refuse_handling_fire_protection']
            electrical_hazard = form.cleaned_data['electrical_hazard']
            electrical_hazard_location = form.cleaned_data['electrical_hazard_location']
            mechanical_hazard = form.cleaned_data['mechanical_hazard']
            mechanical_hazard_location = form.cleaned_data['mechanical_hazard_location']
            elevator_count = form.cleaned_data['elevator_count']
            other_service_system = form.cleaned_data['other_service_system']
            hazardous_area = form.cleaned_data['hazardous_area']
            hazardous_area_other = form.cleaned_data['hazardous_area_other']
            separation_fire_rated = form.cleaned_data['separation_fire_rated']
            type_of_protection = form.cleaned_data['type_of_protection']
            separation_fire_rated_count = form.cleaned_data['separation_fire_rated_count']
            separation_fire_rated_capacity = form.cleaned_data['separation_fire_rated_capacity']
            separation_fire_rated_accessible = form.cleaned_data['separation_fire_rated_accessible']
            separation_fire_rated_fuel = form.cleaned_data['separation_fire_rated_fuel']
            separation_fire_rated_location = form.cleaned_data['separation_fire_rated_location']
            separation_fire_rated_permit = form.cleaned_data['separation_fire_rated_permit']
            hazardous_material = form.cleaned_data['hazardous_material']
            hazardous_material_stored = form.cleaned_data['hazardous_material_stored']
            fire_brigade_organization = form.cleaned_data['fire_brigade_organization']
            fire_safety_seminar = form.cleaned_data['fire_safety_seminar']
            employee_trained_in_emergency_procedures = form.cleaned_data['employee_trained_in_emergency_procedures']
            evacuation_drill_first = form.cleaned_data['evacuation_drill_first']
            evacuation_drill_second = form.cleaned_data['evacuation_drill_second']
            defects = form.cleaned_data['defects']
            defects_photo = form.cleaned_data['defects_photo']
            recommendations = form.cleaned_data['recommendations']
            building = form.cleaned_data['building']
            business = form.cleaned_data['business']
            building_permit_date_issued = form.cleaned_data['building_permit_date_issued']
            occupancy_permit_date_issued = form.cleaned_data['occupancy_permit_date_issued']
            fsic_date_issued = form.cleaned_data['fsic_date_issued']
            fire_drill_certificate_date_issued = form.cleaned_data['fire_drill_certificate_date_issued']
            violation_control_no_date_issued = form.cleaned_data['violation_control_no_date_issued']
            electrical_inspection_date_issued = form.cleaned_data['electrical_inspection_date_issued']
            insurance_date_issued = form.cleaned_data['insurance_date_issued']
            main_stair_pressurized_stairway_last_tested = form.cleaned_data[
                'main_stair_pressurized_stairway_last_tested']
            fire_door_pressurized_stairway_last_tested = form.cleaned_data['fire_door_pressurized_stairway_last_tested']
            vertical_opening_last_tested = form.cleaned_data['vertical_opening_last_tested']
            fire_hose_last_tested = form.cleaned_data['fire_hose_last_tested']
            sprinkler_system_last_tested = form.cleaned_data['sprinkler_system_last_tested']
            sprinkler_system_last_conducted = form.cleaned_data['sprinkler_system_last_conducted']
            certificate_of_installation_date = form.cleaned_data['certificate_of_installation_date']
            generator_mechanical_permit_date_issued = form.cleaned_data['generator_mechanical_permit_date_issued']
            date_checked = form.cleaned_data['date_checked']

            checklist, checklist_message = Master.objects.create(
                first_name=first_name,
                middle_name=middle_name,
                last_name=last_name,
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
                separation_fire_rated_capacity=separation_fire_rated_capacity,
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
                date_checked=date_checked,
            )

            if checklist:
                messages.success(request, 'Checklist recorded!', extra_tags='success')
                return HttpResponseRedirect(reverse('admin_dashboard_checklist_detail', kwargs={'pk': checklist.pk}))
            else:
                messages.error(request, checklist_message, extra_tags='danger')
        else:
            messages.error(request, form.errors, extra_tags='danger')
            request.session['checklist_formdata'] = checklist_formdata

        return HttpResponseRedirect(reverse('admin_dashboard_checklist_create'))


class AdminDashboardChecklistDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Checklist.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))

        context = {
            "page_title": f"Checklist: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj,
        }

        return render(request, "checklist/detail.html", context)


class AdminDashboardChecklistUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Checklist.

    Allowed HTTP verbs:
        - GET
        - POST

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update Checklist: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "checklist/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        form = MasterForm(instance=obj, data=request.POST)

        if form.is_valid():
            data = form.save()
            messages.success(
                request,
                f'{data} saved!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'admin_dashboard_checklist_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update Checklist: {obj}",
                "menu_section": "admin_dashboards",
                "menu_subsection": "admin_dashboards",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "checklist/form.html", context)


class AdminDashboardChecklistDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Checklist.

    Allowed HTTP verbs:
        - GET
        - POST

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        context = {
            "page_title": f"Delete Checklist: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "checklist/delete.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_checklist_list'
            )
        )
