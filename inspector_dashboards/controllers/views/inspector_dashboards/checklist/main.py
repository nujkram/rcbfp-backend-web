from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from accounts.mixins.user_type_mixins import IsUserViewMixin
from buildings.constants import LOCATION_CHOICES, CURRENT_CHOICES, FUEL_CHOICES, CONTAINER_LOCATION_CHOICES, \
    GENERATOR_DISPENSING_CHOICES, GENERATOR_TYPE_CHOICES, SERVICE_SYSTEM_CHOICES, HAZARDOUS_AREA_CHOICES
from business.models import Business
from checklists.constants import REINSPECT, APPROVED, FAILED
from checklists.models import Checklist as Master
from inspections.constants import DONE
from inspections.models import InspectionSchedule
from inspector_dashboards.controllers.views.inspector_dashboards.checklist.forms import ChecklistForm as MasterForm

"""
URLS
# Checklist

from inspector_dashboards.controllers.views.inspector_dashboards.checklist import main as checklist_views

urlpatterns += {
    path(
        'checklist/list',
        checklist_views.InspectorDashboardChecklistListView.as_view(),
        name='inspector_dashboard_checklist_list'
    ),
    path(
        'checklist/<pk>/detail',
        checklist_views.InspectorDashboardChecklistDetailView.as_view(),
        name='inspector_dashboard_checklist_detail'
    ),
    path(
        'checklist/create',
        checklist_views.InspectorDashboardChecklistCreateView.as_view(),
        name='inspector_dashboard_checklist_create'
    ),
    path(
        'checklist/<pk>/update',
        checklist_views.InspectorDashboardChecklistUpdateView.as_view(),
        name='inspector_dashboard_checklist_update'
    ),
    path(
        'checklist/<pk>/delete',
        checklist_views.InspectorDashboardChecklistDeleteView.as_view(),
        name='inspector_dashboard_checklist_delete'
    )
}
"""


class InspectorDashboardChecklistListView(LoginRequiredMixin, IsUserViewMixin, View):
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
            "menu_section": "user_dashboards",
            "menu_subsection": "user_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "inspector_dashboard/checklist/list.html", context)


class InspectorDashboardChecklistCreateView(LoginRequiredMixin, IsUserViewMixin, View):
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
        inspection_schedule = InspectionSchedule.objects.get(pk=pk)
        business = Business.objects.get(pk=inspection_schedule.business.pk)

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
                'exits_count': '',
                'exits_width': '',
                'exits_accessible': '',
                'termination_of_exit': '',
                'exits_enclosure_provided': '',
                'exits_enclosure_construction': '',
                'exits_fire_doors_provided': '',
                'exits_fire_door_construction': '',
                'stairs_count': '',
                'stairs_enclosure_provided': '',
                'stairs_enclosure_construction': '',
                'stairs_fire_doors_provided': '',
                'stairs_fire_door_construction': '',
                'other_details': '',
                'emergency_light': '',
                'exit_signs_illuminated': '',
                'fire_extinguisher_count': '',
                'fire_extinguisher_accessible': '',
                'fire_extinguisher_conspicuous_location': '',
                'fire_alarm': '',
                'detectors': '',
                'control_panel_location': '',
                'control_panel_functional': '',
                'hazardous_materials': '',
                'hazardous_materials_properly_stored': '',
                'no_smoking_sign': '',
                'smoking_permitted': '',
                'smoking_area_location': '',
                'storage_location': '',
                'safety_device_for_lpg': '',
                'oven_used': '',
                'kind_of_fuel': '',
                'smoke_hood': '',
                'spark_arrester': '',
                'partition_construction': '',
                'defects': '',
                'building_permit_date_issued': '',
                'occupancy_permit_date_issued': '',
                'fsic_date_issued': '',
                'fire_drill_certificate_date_issued': '',
                'violation_control_no_date_issued': '',
                'electrical_inspection_date_issued': '',
                'insurance_date_issued': '',
                'notes': '',
                'recommendations': '',
            }

        context = {
            "page_title": "Create new Checklist",
            "menu_section": "user_dashboards",
            "menu_subsection": "user_dashboards",
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
            "inspection_schedule": inspection_schedule,
        }

        return render(request, "inspector_dashboard/checklist/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(request.POST, request.FILES)
        pk = kwargs.get('pk', None)

        inspection_schedule = InspectionSchedule.objects.get(pk=pk)

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
            'exits_count': request.POST.get('exits_count', ''),
            'exits_width': request.POST.get('exits_width', ''),
            'exits_accessible': request.POST.get('exits_accessible', ''),
            'termination_of_exit': request.POST.get('termination_of_exit', ''),
            'exits_enclosure_provided': request.POST.get('exits_enclosure_provided', ''),
            'exits_enclosure_construction': request.POST.get('exits_enclosure_construction', ''),
            'exits_fire_doors_provided': request.POST.get('exits_fire_doors_provided', ''),
            'exits_fire_door_construction': request.POST.get('exits_fire_door_construction', ''),
            'stairs_count': request.POST.get('stairs_count', ''),
            'stairs_enclosure_provided': request.POST.get('stairs_enclosure_provided', ''),
            'stairs_enclosure_construction': request.POST.get('stairs_enclosure_construction', ''),
            'stairs_fire_doors_provided': request.POST.get('stairs_fire_doors_provided', ''),
            'stairs_fire_door_construction': request.POST.get('stairs_fire_door_construction', ''),
            'other_details': request.POST.get('other_details', ''),
            'emergency_light': request.POST.get('emergency_light', ''),
            'exit_signs_illuminated': request.POST.get('exit_signs_illuminated', ''),
            'fire_extinguisher_count': request.POST.get('fire_extinguisher_count', ''),
            'fire_extinguisher_accessible': request.POST.get('fire_extinguisher_accessible', ''),
            'fire_extinguisher_conspicuous_location': request.POST.get('fire_extinguisher_conspicuous_location', ''),
            'fire_alarm': request.POST.get('fire_alarm', ''),
            'detectors': request.POST.get('detectors', ''),
            'control_panel_location': request.POST.get('control_panel_location', ''),
            'control_panel_functional': request.POST.get('control_panel_functional', ''),
            'hazardous_materials': request.POST.get('hazardous_materials', ''),
            'hazardous_materials_properly_stored': request.POST.get('hazardous_materials_properly_stored', ''),
            'no_smoking_sign': request.POST.get('no_smoking_sign', ''),
            'smoking_permitted': request.POST.get('smoking_permitted', ''),
            'smoking_area_location': request.POST.get('smoking_area_location', ''),
            'storage_location': request.POST.get('storage_location', ''),
            'safety_device_for_lpg': request.POST.get('safety_device_for_lpg', ''),
            'oven_used': request.POST.get('oven_used', ''),
            'kind_of_fuel': request.POST.get('kind_of_fuel', ''),
            'smoke_hood': request.POST.get('smoke_hood', ''),
            'spark_arrester': request.POST.get('spark_arrester', ''),
            'partition_construction': request.POST.get('partition_construction', ''),
            'defects': request.POST.get('defects', ''),
            'building_permit_date_issued': request.POST.get('building_permit_date_issued', ''),
            'occupancy_permit_date_issued': request.POST.get('occupancy_permit_date_issued', ''),
            'fsic_date_issued': request.POST.get('fsic_date_issued', ''),
            'fire_drill_certificate_date_issued': request.POST.get('fire_drill_certificate_date_issued', ''),
            'violation_control_no_date_issued': request.POST.get('violation_control_no_date_issued', ''),
            'electrical_inspection_date_issued': request.POST.get('electrical_inspection_date_issued', ''),
            'insurance_date_issued': request.POST.get('insurance_date_issued', ''),
            'date_checked': request.POST.get('date_checked', ''),
            'building': request.POST.get('building', ''),
            'business': request.POST.get('business', ''),
            'notes': request.POST.get('notes', ''),
            'recommendations': request.POST.get('recommendations', ''),
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
            exits_count = form.cleaned_data['exits_count']
            exits_width = form.cleaned_data['exits_width']
            exits_accessible = form.cleaned_data['exits_accessible']
            termination_of_exit = form.cleaned_data['termination_of_exit']
            exits_enclosure_provided = form.cleaned_data['exits_enclosure_provided']
            exits_enclosure_construction = form.cleaned_data['exits_enclosure_construction']
            exits_fire_doors_provided = form.cleaned_data['exits_fire_doors_provided']
            exits_fire_door_construction = form.cleaned_data['exits_fire_door_construction']
            stairs_count = form.cleaned_data['stairs_count']
            stairs_enclosure_provided = form.cleaned_data['stairs_enclosure_provided']
            stairs_enclosure_construction = form.cleaned_data['stairs_enclosure_construction']
            stairs_fire_doors_provided = form.cleaned_data['stairs_fire_doors_provided']
            stairs_fire_door_construction = form.cleaned_data['stairs_fire_door_construction']
            other_details = form.cleaned_data['other_details']
            emergency_light = form.cleaned_data['emergency_light']
            exit_signs_illuminated = form.cleaned_data['exit_signs_illuminated']
            fire_extinguisher_count = form.cleaned_data['fire_extinguisher_count']
            fire_extinguisher_accessible = form.cleaned_data['fire_extinguisher_accessible']
            fire_extinguisher_conspicuous_location = form.cleaned_data['fire_extinguisher_conspicuous_location']
            fire_alarm = form.cleaned_data['fire_alarm']
            detectors = form.cleaned_data['detectors']
            control_panel_location = form.cleaned_data['control_panel_location']
            control_panel_functional = form.cleaned_data['control_panel_functional']
            hazardous_materials = form.cleaned_data['hazardous_materials']
            hazardous_materials_properly_stored = form.cleaned_data['hazardous_materials_properly_stored']
            no_smoking_sign = form.cleaned_data['no_smoking_sign']
            smoking_permitted = form.cleaned_data['smoking_permitted']
            smoking_area_location = form.cleaned_data['smoking_area_location']
            storage_location = form.cleaned_data['storage_location']
            safety_device_for_lpg = form.cleaned_data['safety_device_for_lpg']
            oven_used = form.cleaned_data['oven_used']
            kind_of_fuel = form.cleaned_data['kind_of_fuel']
            smoke_hood = form.cleaned_data['smoke_hood']
            spark_arrester = form.cleaned_data['spark_arrester']
            partition_construction = form.cleaned_data['partition_construction']
            defects = form.cleaned_data['defects']
            building_permit_date_issued = form.cleaned_data['building_permit_date_issued']
            occupancy_permit_date_issued = form.cleaned_data['occupancy_permit_date_issued']
            fsic_date_issued = form.cleaned_data['fsic_date_issued']
            fire_drill_certificate_date_issued = form.cleaned_data['fire_drill_certificate_date_issued']
            violation_control_no_date_issued = form.cleaned_data['violation_control_no_date_issued']
            electrical_inspection_date_issued = form.cleaned_data['electrical_inspection_date_issued']
            insurance_date_issued = form.cleaned_data['insurance_date_issued']
            date_checked = form.cleaned_data['date_checked']
            building = form.cleaned_data['building']
            business = form.cleaned_data['business']
            notes = form.cleaned_data['notes']
            recommendations = form.cleaned_data['recommendations']

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
                exits_count=exits_count,
                exits_width=exits_width,
                exits_accessible=exits_accessible,
                termination_of_exit=termination_of_exit,
                exits_enclosure_provided=exits_enclosure_provided,
                exits_enclosure_construction=exits_enclosure_construction,
                exits_fire_doors_provided=exits_fire_doors_provided,
                exits_fire_door_construction=exits_fire_door_construction,
                stairs_count=stairs_count,
                stairs_enclosure_provided=stairs_enclosure_provided,
                stairs_enclosure_construction=stairs_enclosure_construction,
                stairs_fire_doors_provided=stairs_fire_doors_provided,
                stairs_fire_door_construction=stairs_fire_door_construction,
                other_details=other_details,
                emergency_light=emergency_light,
                exit_signs_illuminated=exit_signs_illuminated,
                fire_extinguisher_count=fire_extinguisher_count,
                fire_extinguisher_accessible=fire_extinguisher_accessible,
                fire_extinguisher_conspicuous_location=fire_extinguisher_conspicuous_location,
                fire_alarm=fire_alarm,
                detectors=detectors,
                control_panel_location=control_panel_location,
                control_panel_functional=control_panel_functional,
                hazardous_materials=hazardous_materials,
                hazardous_materials_properly_stored=hazardous_materials_properly_stored,
                no_smoking_sign=no_smoking_sign,
                smoking_permitted=smoking_permitted,
                smoking_area_location=smoking_area_location,
                storage_location=storage_location,
                safety_device_for_lpg=safety_device_for_lpg,
                oven_used=oven_used,
                kind_of_fuel=kind_of_fuel,
                smoke_hood=smoke_hood,
                spark_arrester=spark_arrester,
                partition_construction=partition_construction,
                defects=defects,
                building_permit_date_issued=building_permit_date_issued,
                occupancy_permit_date_issued=occupancy_permit_date_issued,
                fsic_date_issued=fsic_date_issued,
                fire_drill_certificate_date_issued=fire_drill_certificate_date_issued,
                violation_control_no_date_issued=violation_control_no_date_issued,
                electrical_inspection_date_issued=electrical_inspection_date_issued,
                insurance_date_issued=insurance_date_issued,
                date_checked=date_checked,
                building=building,
                business=business,
                notes=notes,
                recommendations=recommendations,
            )

            if checklist:
                result = checklist.result()
                if result:
                    checklist.status = APPROVED
                    checklist.remarks = APPROVED

                    is_safe = checklist.business.is_safe(checklist_pk=checklist.pk)
                    if is_safe:
                        checklist.business.status = APPROVED
                        checklist.building.status = APPROVED
                    else:
                        checklist.business.status = FAILED
                        checklist.building.status = FAILED
                    checklist.business.save()
                    checklist.building.save()
                else:
                    checklist.remarks = REINSPECT
                    checklist.status = FAILED

                checklist.inspection = inspection_schedule
                checklist.save()

                if inspection_schedule.inspection_type == REINSPECT:
                    if checklist.remarks == REINSPECT:
                        checklist.status = FAILED
                        checklist.remarks = REINSPECT
                        checklist.save()

                inspection_schedule.status = DONE
                inspection_schedule.save()

                messages.success(request, 'Checklist recorded!', extra_tags='success')
                return HttpResponseRedirect(
                    reverse('inspector_dashboard_checklist_detail', kwargs={'pk': checklist.pk}))
            else:
                messages.error(request, checklist_message, extra_tags='danger')
        else:
            messages.error(request, form.errors, extra_tags='danger')
            request.session['checklist_formdata'] = checklist_formdata

        return HttpResponseRedirect(reverse('inspector_dashboard_checklist_create', kwargs={'pk': pk}))


class InspectorDashboardChecklistDetailView(LoginRequiredMixin, IsUserViewMixin, View):
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
            "menu_section": "user_dashboards",
            "menu_subsection": "user_dashboards",
            "menu_action": "detail",
            "obj": obj,
        }

        return render(request, "inspector_dashboard/checklist/detail.html", context)


class InspectorDashboardChecklistUpdateView(LoginRequiredMixin, IsUserViewMixin, View):
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
            "menu_section": "user_dashboards",
            "menu_subsection": "user_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "inspector_dashboard/checklist/form.html", context)

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
                    'inspector_dashboard_checklist_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update Checklist: {obj}",
                "menu_section": "user_dashboards",
                "menu_subsection": "user_dashboards",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "inspector_dashboard/checklist/form.html", context)


class InspectorDashboardChecklistDeleteView(LoginRequiredMixin, IsUserViewMixin, View):
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
            "menu_section": "user_dashboards",
            "menu_subsection": "user_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "inspector_dashboard/checklist/delete.html", context)

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
                'inspector_dashboard_checklist_list'
            )
        )
