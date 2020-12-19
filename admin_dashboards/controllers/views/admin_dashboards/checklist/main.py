from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from buildings.constants import LOCATION_CHOICES, CURRENT_CHOICES, FUEL_CHOICES, CONTAINER_LOCATION_CHOICES, \
    GENERATOR_DISPENSING_CHOICES, GENERATOR_TYPE_CHOICES, SERVICE_SYSTEM_CHOICES, HAZARDOUS_AREA_CHOICES
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
        'checklist/<pk>/update',
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
    # ERROR FOLLOW INSPECTOR CHECKLIST CREATE VIEW
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
        pk = kwargs.get('pk', None)

        if pk:
            business = Business.objects.get(pk=pk)

        location_choices = LOCATION_CHOICES
        current_choices = CURRENT_CHOICES
        fuel_choices = FUEL_CHOICES
        container_location_choices = CONTAINER_LOCATION_CHOICES
        generator_dispensing_choices = GENERATOR_DISPENSING_CHOICES
        generator_type_choices = GENERATOR_TYPE_CHOICES
        service_system_choices = SERVICE_SYSTEM_CHOICES
        hazardous_area_choices = HAZARDOUS_AREA_CHOICES

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
            "fuel_choices": fuel_choices,
            "container_location_choices": container_location_choices,
            "generator_dispensing_choices": generator_dispensing_choices,
            "generator_type_choices": generator_type_choices,
            "service_system_choices": service_system_choices,
            "hazardous_area_choices": hazardous_area_choices,
            "business": business,
        }

        return render(request, "checklist/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(request.POST, request.FILES)
        pk = kwargs.get('pk', None)

        checklist_formdata = {
            'first_name': request.POST.get('first_name', ''),
            'middle_name': request.POST.get('middle_name', ''),
            'last_name': request.POST.get('last_name', ''),
            'policy_no': request.POST.get('policy_no', ''),
            'building_permit': request.POST.get('building_permit', ''),
            'occupancy_permit': request.POST.get('occupancy_permit', ''),
            'fsic_control_no': request.POST.get('fsic_control_no', ''),
            'fsic_fee': request.POST.get('fsic_fee', ''),
            'fire_drill_certificate': request.POST.get('fire_drill_certificate', ''),
            'violation_control_no': request.POST.get('violation_control_no', ''),
            'electrical_inspection_no': request.POST.get('electrical_inspection_no', ''),
            'sectional_occupancy': request.POST.get('sectional_occupancy', ''),
            'occupant_load': request.POST.get('occupant_load', ''),
            'egress_capacity': request.POST.get('egress_capacity', ''),
            'any_renovation': request.POST.get('any_renovation', ''),
            'renovation_specification': request.POST.get('renovation_specification', ''),
            'horizontal_exit_capacity': request.POST.get('horizontal_exit_capacity', ''),
            'exit_stair_capacity': request.POST.get('exit_stair_capacity', ''),
            'no_of_exits': request.POST.get('no_of_exits', ''),
            'is_exits_remote': request.POST.get('is_exits_remote', ''),
            'exit_location': request.POST.get('exit_location', ''),
            'any_enclosure': request.POST.get('any_enclosure', ''),
            'is_exit_accessible': request.POST.get('is_exit_accessible', ''),
            'is_fire_doors_provided': request.POST.get('is_fire_doors_provided', ''),
            'self_closing_mechanism': request.POST.get('self_closing_mechanism', ''),
            'panic_hardware': request.POST.get('panic_hardware', ''),
            'readily_accessible': request.POST.get('readily_accessible', ''),
            'travel_distance_within_limit': request.POST.get('travel_distance_within_limit', ''),
            'adequate_illumination': request.POST.get('adequate_illumination', ''),
            'panic_hardware_operational': request.POST.get('panic_hardware_operational', ''),
            'doors_open_easily': request.POST.get('doors_open_easily', ''),
            'bldg_with_mezzanine': request.POST.get('bldg_with_mezzanine', ''),
            'is_obstructed': request.POST.get('is_obstructed', ''),
            'dead_ends_within_limits': request.POST.get('dead_ends_within_limits', ''),
            'proper_rating_illumination': request.POST.get('proper_rating_illumination', ''),
            'door_swing_in_the_direction_of_exit': request.POST.get('door_swing_in_the_direction_of_exit', ''),
            'self_closure_operational': request.POST.get('self_closure_operational', ''),
            'mezzanine_with_proper_exits': request.POST.get('mezzanine_with_proper_exits', ''),
            'corridors_of_sufficient_size': request.POST.get('corridors_of_sufficient_size', ''),
            'main_stair_width': request.POST.get('main_stair_width', ''),
            'construction': request.POST.get('construction', ''),
            'main_stair_railings': request.POST.get('main_stair_railings', ''),
            'main_stair_railings_built': request.POST.get('main_stair_railings_built', ''),
            'main_stair_any_enclosure_provided': request.POST.get('main_stair_any_enclosure_provided', ''),
            'enclosure_built': request.POST.get('enclosure_built', ''),
            'any_openings': request.POST.get('any_openings', ''),
            'main_stair_door_proper_rating': request.POST.get('main_stair_door_proper_rating', ''),
            'main_stair_door_provided_with_vision_panel': request.POST.get('main_stair_door_provided_with_vision_panel',
                                                                           ''),
            'main_stair_door_vision_panel_built': request.POST.get('main_stair_door_vision_panel_built', ''),
            'main_stair_pressurized_stairway': request.POST.get('main_stair_pressurized_stairway', ''),
            'main_stair_type_of_pressurized_stairway': request.POST.get('main_stair_type_of_pressurized_stairway', ''),
            'fire_escape_count': request.POST.get('fire_escape_count', ''),
            'fire_escape_width': request.POST.get('fire_escape_width', ''),
            'fire_escape_construction': request.POST.get('fire_escape_construction', ''),
            'fire_escape_railings': request.POST.get('fire_escape_railings', ''),
            'fire_escape_built': request.POST.get('fire_escape_built', ''),
            'fire_escape_location': request.POST.get('fire_escape_location', ''),
            'fire_escape_obstruction': request.POST.get('fire_escape_obstruction', ''),
            'discharge_of_exits': request.POST.get('discharge_of_exits', ''),
            'fire_escape_any_enclosure_provided': request.POST.get('fire_escape_any_enclosure_provided', ''),
            'fire_escape_enclosure': request.POST.get('fire_escape_enclosure', ''),
            'fire_escape_opening': request.POST.get('fire_escape_opening', ''),
            'fire_escape_opening_protected': request.POST.get('fire_escape_opening_protected', ''),
            'fire_door_provided': request.POST.get('fire_door_provided', ''),
            'fire_door_width': request.POST.get('fire_door_width', ''),
            'fire_door_construction': request.POST.get('fire_door_construction', ''),
            'fire_door_door_proper_rating': request.POST.get('fire_door_door_proper_rating', ''),
            'fire_door_door_provided_with_vision_panel': request.POST.get('fire_door_door_provided_with_vision_panel',
                                                                          ''),
            'fire_door_door_vision_panel_built': request.POST.get('fire_door_door_vision_panel_built', ''),
            'fire_door_pressurized_stairway': request.POST.get('fire_door_pressurized_stairway', ''),
            'fire_door_type_of_pressurized_stairway': request.POST.get('fire_door_type_of_pressurized_stairway', ''),
            'horizontal_exit_width': request.POST.get('horizontal_exit_width', ''),
            'horizontal_exit_construction': request.POST.get('horizontal_exit_construction', ''),
            'horizontal_exit_vision_panel': request.POST.get('horizontal_exit_vision_panel', ''),
            'horizontal_exit_door_swing_in_direction_of_egress': request.POST.get(
                'horizontal_exit_door_swing_in_direction_of_egress', ''),
            'horizontal_exit_with_self_closing_device': request.POST.get('horizontal_exit_with_self_closing_device',
                                                                         ''),
            'horizontal_exit_corridor_width': request.POST.get('horizontal_exit_corridor_width', ''),
            'horizontal_exit_corridor_construction': request.POST.get('horizontal_exit_corridor_construction', ''),
            'horizontal_exit_corridor_walls_extended': request.POST.get('horizontal_exit_corridor_walls_extended', ''),
            'horizontal_exit_properly_illuminated': request.POST.get('horizontal_exit_properly_illuminated', ''),
            'horizontal_exit_readily_visible': request.POST.get('horizontal_exit_readily_visible', ''),
            'horizontal_exit_properly_marked': request.POST.get('horizontal_exit_properly_marked', ''),
            'horizontal_exit_with_illuminated_directional_sign': request.POST.get(
                'horizontal_exit_with_illuminated_directional_sign', ''),
            'horizontal_exit_properly_located': request.POST.get('horizontal_exit_properly_located', ''),
            'ramps_provided': request.POST.get('ramps_provided', ''),
            'ramps_type': request.POST.get('ramps_type', ''),
            'ramps_width': request.POST.get('ramps_width', ''),
            'ramps_class': request.POST.get('ramps_class', ''),
            'ramps_railing_provided': request.POST.get('ramps_railing_provided', ''),
            'ramps_height': request.POST.get('ramps_height', ''),
            'ramps_enclosure': request.POST.get('ramps_enclosure', ''),
            'ramps_construction': request.POST.get('ramps_construction', ''),
            'ramps_fire_doors': request.POST.get('ramps_fire_doors', ''),
            'ramps_fire_doors_width': request.POST.get('ramps_fire_doors_width', ''),
            'ramps_fire_doors_construction': request.POST.get('ramps_fire_doors_construction', ''),
            'ramps_with_self_closing_device': request.POST.get('ramps_with_self_closing_device', ''),
            'ramps_door_with_proper_rating': request.POST.get('ramps_door_with_proper_rating', ''),
            'ramps_door_with_vision_panel': request.POST.get('ramps_door_with_vision_panel', ''),
            'ramps_door_vision_panel_built': request.POST.get('ramps_door_vision_panel_built', ''),
            'ramps_door_swing_in_direction_of_egress': request.POST.get('ramps_door_swing_in_direction_of_egress', ''),
            'ramps_obstruction': request.POST.get('ramps_obstruction', ''),
            'ramps_discharge_of_exit': request.POST.get('ramps_discharge_of_exit', ''),
            'safe_refuge_provided': request.POST.get('safe_refuge_provided', ''),
            'safe_refuge_type': request.POST.get('safe_refuge_type', ''),
            'safe_refuge_enclosure': request.POST.get('safe_refuge_enclosure', ''),
            'safe_refuge_construction': request.POST.get('safe_refuge_construction', ''),
            'safe_refuge_fire_door': request.POST.get('safe_refuge_fire_door', ''),
            'safe_refuge_fire_door_width': request.POST.get('safe_refuge_fire_door_width', ''),
            'safe_refuge_fire_door_construction': request.POST.get('safe_refuge_fire_door_construction', ''),
            'safe_refuge_with_self_closing_device': request.POST.get('safe_refuge_with_self_closing_device', ''),
            'safe_refuge_door_proper_rating': request.POST.get('safe_refuge_door_proper_rating', ''),
            'safe_refuge_with_vision_panel': request.POST.get('safe_refuge_with_vision_panel', ''),
            'safe_refuge_vision_panel_built': request.POST.get('safe_refuge_vision_panel_built', ''),
            'safe_refuge_swing_in_direction_of_egress': request.POST.get('safe_refuge_swing_in_direction_of_egress',
                                                                         ''),
            'emergency_light': request.POST.get('emergency_light', ''),
            'emergency_light_source': request.POST.get('emergency_light_source', ''),
            'emergency_light_per_floor_count': request.POST.get('emergency_light_per_floor_count', ''),
            'emergency_light_hallway_count': request.POST.get('emergency_light_hallway_count', ''),
            'emergency_light_stairway_count': request.POST.get('emergency_light_stairway_count', ''),
            'emergency_light_operational': request.POST.get('emergency_light_operational', ''),
            'emergency_light_exit_path_properly_illuminated': request.POST.get(
                'emergency_light_exit_path_properly_illuminated', ''),
            'emergency_light_tested_monthly': request.POST.get('emergency_light_tested_monthly', ''),
            'exit_signs_illuminated': request.POST.get('exit_signs_illuminated', ''),
            'exit_signs_location': request.POST.get('exit_signs_location', ''),
            'exit_signs_source': request.POST.get('exit_signs_source', ''),
            'exit_signs_visible': request.POST.get('exit_signs_visible', ''),
            'exit_signs_min_letter_size': request.POST.get('exit_signs_min_letter_size', ''),
            'exit_route_posted_on_lobby': request.POST.get('exit_route_posted_on_lobby', ''),
            'exit_route_posted_on_rooms': request.POST.get('exit_route_posted_on_rooms', ''),
            'directional_exit_signs': request.POST.get('directional_exit_signs', ''),
            'directional_exit_signs_location': request.POST.get('directional_exit_signs_location', ''),
            'no_smoking_sign': request.POST.get('no_smoking_sign', ''),
            'dead_end_sign': request.POST.get('dead_end_sign', ''),
            'elevator_sign': request.POST.get('elevator_sign', ''),
            'keep_door_closed_sign': request.POST.get('keep_door_closed_sign', ''),
            'others': request.POST.get('others', ''),
            'vertical_openings_properly_protected': request.POST.get('vertical_openings_properly_protected', ''),
            'vertical_openings_atrium': request.POST.get('vertical_openings_atrium', ''),
            'fire_doors_good_condition': request.POST.get('fire_doors_good_condition', ''),
            'elevator_opening_protected': request.POST.get('elevator_opening_protected', ''),
            'pipe_chase_opening_protected': request.POST.get('pipe_chase_opening_protected', ''),
            'aircon_ducts_with_dumper': request.POST.get('aircon_ducts_with_dumper', ''),
            'garbage_chute_protected': request.POST.get('garbage_chute_protected', ''),
            'between_floor_protected': request.POST.get('between_floor_protected', ''),
            'standpipe_type': request.POST.get('standpipe_type', ''),
            'standpipe_tank_capacity': request.POST.get('standpipe_tank_capacity', ''),
            'standpipe_location': request.POST.get('standpipe_location', ''),
            'siamese_intake_provided': request.POST.get('siamese_intake_provided', ''),
            'siamese_intake_location': request.POST.get('siamese_intake_location', ''),
            'siamese_intake_size': request.POST.get('siamese_intake_size', ''),
            'siamese_intake_count': request.POST.get('siamese_intake_count', ''),
            'siamese_intake_accessible': request.POST.get('siamese_intake_accessible', ''),
            'fire_hose_cabinet': request.POST.get('fire_hose_cabinet', ''),
            'fire_hose_cabinet_accessories': request.POST.get('fire_hose_cabinet_accessories', ''),
            'fire_hose_cabinet_location': request.POST.get('fire_hose_cabinet_location', ''),
            'fire_hose_per_floor_count': request.POST.get('fire_hose_per_floor_count', ''),
            'fire_hose_size': request.POST.get('fire_hose_size', ''),
            'fire_hose_length': request.POST.get('fire_hose_length', ''),
            'fire_hose_nozzle': request.POST.get('fire_hose_nozzle', ''),
            'fire_lane': request.POST.get('fire_lane', ''),
            'fire_hydrant_location': request.POST.get('fire_hydrant_location', ''),
            'portable_fire_extinguisher_type': request.POST.get('portable_fire_extinguisher_type', ''),
            'portable_fire_extinguisher_capacity': request.POST.get('portable_fire_extinguisher_capacity', ''),
            'portable_fire_extinguisher_count': request.POST.get('portable_fire_extinguisher_count', ''),
            'portable_fire_extinguisher_with_ps_mark': request.POST.get('portable_fire_extinguisher_with_ps_mark', ''),
            'portable_fire_extinguisher_with_iso_mark': request.POST.get('portable_fire_extinguisher_with_iso_mark',
                                                                         ''),
            'portable_fire_extinguisher_maintained': request.POST.get('portable_fire_extinguisher_maintained', ''),
            'portable_fire_extinguisher_conspicuously_located': request.POST.get(
                'portable_fire_extinguisher_conspicuously_located', ''),
            'portable_fire_extinguisher_accessible': request.POST.get('portable_fire_extinguisher_accessible', ''),
            'portable_fire_extinguisher_other_type': request.POST.get('portable_fire_extinguisher_other_type', ''),
            'sprinkler_system_agent_used': request.POST.get('sprinkler_system_agent_used', ''),
            'jockey_pump_capacity': request.POST.get('jockey_pump_capacity', ''),
            'fire_pump_capacity': request.POST.get('fire_pump_capacity', ''),
            'gpm_tank_capacity': request.POST.get('gpm_tank_capacity', ''),
            'maintaining_line_pressure': request.POST.get('maintaining_line_pressure', ''),
            'farthest_sprinkler_head_pressure': request.POST.get('farthest_sprinkler_head_pressure', ''),
            'riser_size': request.POST.get('riser_size', ''),
            'type_of_heads_installed': request.POST.get('type_of_heads_installed', ''),
            'heads_per_floor_count': request.POST.get('heads_per_floor_count', ''),
            'heads_total_count': request.POST.get('heads_total_count', ''),
            'spacing_of_heads': request.POST.get('spacing_of_heads', ''),
            'location_of_fire_dept_connection': request.POST.get('location_of_fire_dept_connection', ''),
            'plan_submitted': request.POST.get('plan_submitted', ''),
            'firewall_required': request.POST.get('firewall_required', ''),
            'firewall_provided': request.POST.get('firewall_provided', ''),
            'firewall_opening': request.POST.get('firewall_opening', ''),
            'boiler_provided': request.POST.get('boiler_provided', ''),
            'boiler_unit_count': request.POST.get('boiler_unit_count', ''),
            'boiler_fuel': request.POST.get('boiler_fuel', ''),
            'boiler_capacity': request.POST.get('boiler_capacity', ''),
            'boiler_container': request.POST.get('boiler_container', ''),
            'boiler_location': request.POST.get('boiler_location', ''),
            'lpg_installation_with_permit': request.POST.get('lpg_installation_with_permit', ''),
            'fuel_with_storage_permit': request.POST.get('fuel_with_storage_permit', ''),
            'generator_set': request.POST.get('generator_set', ''),
            'generator_set_type': request.POST.get('generator_set_type', ''),
            'generator_fuel': request.POST.get('generator_fuel', ''),
            'generator_capacity': request.POST.get('generator_capacity', ''),
            'generator_location': request.POST.get('generator_location', ''),
            'generator_bound_on_wall': request.POST.get('generator_bound_on_wall', ''),
            'generator_container': request.POST.get('generator_container', ''),
            'generator_dispensing_system': request.POST.get('generator_dispensing_system', ''),
            'generator_output_capacity': request.POST.get('generator_output_capacity', ''),
            'generator_mechanical_permit': request.POST.get('generator_mechanical_permit', ''),
            'generator_fuel_storage_permit': request.POST.get('generator_fuel_storage_permit', ''),
            'generator_others': request.POST.get('generator_others', ''),
            'generator_automatic_transfer_switch': request.POST.get('generator_automatic_transfer_switch', ''),
            'generator_time_interval': request.POST.get('generator_time_interval', ''),
            'refuse_handling': request.POST.get('refuse_handling', ''),
            'refuse_handling_enclosure': request.POST.get('refuse_handling_enclosure', ''),
            'refuse_handling_fire_protection': request.POST.get('refuse_handling_fire_protection', ''),
            'electrical_hazard': request.POST.get('electrical_hazard', ''),
            'electrical_hazard_location': request.POST.get('electrical_hazard_location', ''),
            'mechanical_hazard': request.POST.get('mechanical_hazard', ''),
            'mechanical_hazard_location': request.POST.get('mechanical_hazard_location', ''),
            'elevator_count': request.POST.get('elevator_count', ''),
            'other_service_system': request.POST.get('other_service_system', ''),
            'hazardous_area': request.POST.get('hazardous_area', ''),
            'hazardous_area_other': request.POST.get('hazardous_area_other', ''),
            'separation_fire_rated': request.POST.get('separation_fire_rated', ''),
            'type_of_protection': request.POST.get('type_of_protection', ''),
            'separation_fire_rated_count': request.POST.get('separation_fire_rated_count', ''),
            'separation_fire_rated_accessible': request.POST.get('separation_fire_rated_accessible', ''),
            'separation_fire_rated_fuel': request.POST.get('separation_fire_rated_fuel', ''),
            'separation_fire_rated_location': request.POST.get('separation_fire_rated_location', ''),
            'separation_fire_rated_permit': request.POST.get('separation_fire_rated_permit', ''),
            'hazardous_material': request.POST.get('hazardous_material', ''),
            'hazardous_material_stored': request.POST.get('hazardous_material_stored', ''),
            'fire_brigade_organization': request.POST.get('fire_brigade_organization', ''),
            'fire_safety_seminar': request.POST.get('fire_safety_seminar', ''),
            'employee_trained_in_emergency_procedures': request.POST.get('employee_trained_in_emergency_procedures',
                                                                         ''),
            'evacuation_drill_first': request.POST.get('evacuation_drill_first', ''),
            'evacuation_drill_second': request.POST.get('evacuation_drill_second', ''),
            'defects': request.POST.get('defects', ''),
            'defects_photo': request.POST.get('defects_photo', ''),
            'recommendations': request.POST.get('recommendations', ''),
            'building': request.POST.get('building', ''),
            'business': request.POST.get('business', ''),
            'building_permit_date_issued': request.POST.get('building_permit_date_issued', ''),
            'occupancy_permit_date_issued': request.POST.get('occupancy_permit_date_issued', ''),
            'fsic_date_issued': request.POST.get('fsic_date_issued', ''),
            'fire_drill_certificate_date_issued': request.POST.get('fire_drill_certificate_date_issued', ''),
            'violation_control_no_date_issued': request.POST.get('violation_control_no_date_issued', ''),
            'electrical_inspection_date_issued': request.POST.get('electrical_inspection_date_issued', ''),
            'insurance_date_issued': request.POST.get('insurance_date_issued', ''),
            'main_stair_pressurized_stairway_last_tested': request.POST.get(
                'main_stair_pressurized_stairway_last_tested', ''),
            'fire_door_pressurized_stairway_last_tested': request.POST.get('fire_door_pressurized_stairway_last_tested',
                                                                           ''),
            'vertical_opening_last_tested': request.POST.get('vertical_opening_last_tested', ''),
            'fire_hose_last_tested': request.POST.get('fire_hose_last_tested', ''),
            'sprinkler_system_last_tested': request.POST.get('sprinkler_system_last_tested', ''),
            'sprinkler_system_last_conducted': request.POST.get('sprinkler_system_last_conducted', ''),
            'certificate_of_installation_date': request.POST.get('certificate_of_installation_date', ''),
            'generator_mechanical_permit_date_issued': request.POST.get('generator_mechanical_permit_date_issued', ''),
            'date_checked': request.POST.get('date_checked', ''),
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

        return HttpResponseRedirect(reverse('admin_dashboard_checklist_create_by_business', kwargs={'pk': pk}))


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


class AdminDashboardChecklistSummaryView(LoginRequiredMixin, IsAdminViewMixin, View):
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
            "page_title": f"Checklist Summary: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj,
        }

        return render(request, "checklist/summary.html", context)
