from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from buildings.models.building.building_models import Building
from business.models import Business
from incidents.constants import INCIDENT_TYPE_CHOICES

from incidents.models import Incident as Master
from admin_dashboards.controllers.views.admin_dashboards.incident.forms import IncidentForm as MasterForm
from incidents.models.incident.incident_models import IncidentCoordinate
from locations.models import Region, City, Province

"""
URLS
# Incident

from admin_dashboards.controllers.views.admin_dashboards.incident import main as incident_views

urlpatterns += {
    path(
        'incident/list',
        incident_views.AdminDashboardIncidentListView.as_view(),
        name='admin_dashboard_incident_list'
    ),
    path(
        'incident/<pk>/detail',
        incident_views.AdminDashboardIncidentDetailView.as_view(),
        name='admin_dashboard_incident_detail'
    ),
    path(
        'incident/create',
        incident_views.AdminDashboardIncidentCreateView.as_view(),
        name='admin_dashboard_incident_create'
    ),
    path(
        'incident/<pk>/update',
        incident_views.AdminDashboardIncidentUpdateView.as_view(),
        name='admin_dashboard_incident_update'
    ),
    path(
        'incident/<pk>/delete',
        incident_views.AdminDashboardIncidentDeleteView.as_view(),
        name='admin_dashboard_incident_delete'
    )
}
"""


class AdminDashboardIncidentListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Incidents.

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
            "page_title": f"Incidents",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "incident/list.html", context)


class AdminDashboardIncidentCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Incidents.

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
        default_region = Region.objects.get(pk=6) # Region VI
        default_province = Province.objects.get(pk=22) # Capiz
        default_city = City.objects.get(pk=381)  # Roxas City
        regions = Region.objects.all()
        provinces = Province.objects.filter(region=default_region)
        cities = City.objects.filter(province=default_province)
        incident_type_choices = INCIDENT_TYPE_CHOICES
        buildings = Building.objects.all()
        businesses = Business.objects.all()

        if 'incident_formdata' in request.session:
            incident_formdata = request.session['incident_formdata']
            del request.session['incident_formdata']
        else:
            incident_formdata = {
                'first_name': '',
                'last_name': '',
                'middle_name': '',
                'phone': '',
                'address': '',
                'image': '',
                'incident_type': '',
                'property_damage': '',
                'casualties': '',
                'major_injuries': '',
                'minor_injuries': '',
                'intensity': '',
                'severity': '',
                'duration': '',
                'building': '',
                'business': '',
                'region': '',
                'province': '',
                'city': '',
            }

        context = {
            "page_title": "Create new Incident",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "incident_formdata": incident_formdata,
            "form": form,
            "regions": regions,
            "provinces": provinces,
            "cities": cities,
            "default_region": default_region,
            "default_province": default_province,
            "default_city": default_city,
            "incident_type_choices": incident_type_choices,
            "buildings": buildings,
            "businesses": businesses,
        }

        return render(request, "incident/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(request.POST, request.FILES)


        incident_formdata = {
            'first_name': request.POST.get('first_name', ''),
            'last_name': request.POST.get('last_name', ''),
            'middle_name': request.POST.get('middle_name', ''),
            'phone': request.POST.get('phone', ''),
            'address': request.POST.get('address', ''),
            'image': request.POST.get('image', ''),
            'incident_type': request.POST.get('incident_type', ''),
            'property_damage': request.POST.get('property_damage', ''),
            'casualties': request.POST.get('casualties', ''),
            'major_injuries': request.POST.get('major_injuries', ''),
            'minor_injuries': request.POST.get('minor_injuries', ''),
            'intensity': request.POST.get('intensity', ''),
            'severity': request.POST.get('severity', ''),
            'duration': request.POST.get('duration', ''),
            'building': request.POST.get('building', ''),
            'business': request.POST.get('business', ''),
            'region': request.POST.get('region', ''),
            'province': request.POST.get('province', ''),
            'city': request.POST.get('city', ''),
            'lat': request.POST.get('latitude', ''),
            'lng': request.POST.get('longitude', ''),
        }

        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            middle_name = form.cleaned_data['middle_name']
            phone = form.cleaned_data['phone']
            address = form.cleaned_data['address']
            image = form.cleaned_data['image']
            incident_type = form.cleaned_data['incident_type']
            property_damage = form.cleaned_data['property_damage']
            casualties = form.cleaned_data['casualties']
            major_injuries = form.cleaned_data['major_injuries']
            minor_injuries = form.cleaned_data['minor_injuries']
            intensity = form.cleaned_data['intensity']
            severity = form.cleaned_data['severity']
            building = form.cleaned_data['building']
            business = form.cleaned_data['business']
            duration = form.cleaned_data['duration']
            region = form.cleaned_data['region']
            province = form.cleaned_data['province']
            city = form.cleaned_data['city']
            lat = form.cleaned_data['latitude']
            lng = form.cleaned_data['longitude']

            incident, incident_message = Master.objects.create(
                first_name=first_name,
                last_name=last_name,
                middle_name=middle_name,
                phone=phone,
                address=address,
                image=image,
                incident_type=incident_type,
                property_damage=property_damage,
                casualties=casualties,
                major_injuries=major_injuries,
                minor_injuries=minor_injuries,
                intensity=intensity,
                severity=severity,
                duration=duration,
                building=building,
                business=business,
                region=region,
                province=province,
                city=city,
            )

            if incident:
                IncidentCoordinate.objects.create(
                    lat=lat,
                    lng=lng,
                    incident=incident,
                )
                messages.success(request, 'Incident recorded!', extra_tags='success')
                return HttpResponseRedirect(reverse('admin_dashboard_incident_detail', kwargs={'pk': incident.pk}))
            else:
                messages.error(request, incident_message, extra_tags='danger')
        else:
            messages.error(request, form.errors, extra_tags='danger')
            request.session['incident_formdata'] = incident_formdata

        return HttpResponseRedirect(reverse('admin_dashboard_incident_create'))


class AdminDashboardIncidentDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Incidents.

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
        try:
            coords = IncidentCoordinate.objects.get(incident=obj)
        except:
            coords = {
                'lat': obj.building.latitude,
                'lng': obj.building.longitude,
            }

        context = {
            "page_title": f"Incident: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj,
            "coords": coords,
        }

        return render(request, "incident/detail.html", context)


class AdminDashboardIncidentUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Incidents.

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
            "page_title": f"Update Incident: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "incident/form.html", context)

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
                    'admin_dashboard_incident_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update Incident: {obj}",
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
            return render(request, "incident/form.html", context)


class AdminDashboardIncidentDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Incidents.

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
            "page_title": f"Delete Incident: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "incident/delete.html", context)

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
                'admin_dashboard_incident_list'
            )
        )
