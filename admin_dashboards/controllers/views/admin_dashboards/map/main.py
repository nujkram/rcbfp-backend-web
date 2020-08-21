from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from buildings.models.building.building_models import Building

"""
URLS
# Map

from admin_dashboards.controllers.views.admin_dashboards.map import main as map_views

urlpatterns += {
    path(
        'map/buildings',
        map_views.AdminDashboardMapBuildingView.as_view(),
        name='admin_dashboard_map_building_view'
    ),
    path(
        'map/incidents',
        map_views.AdminDashboardMapIncidentView.as_view(),
        name='admin_dashboard_map_incident_view'
    ),
}
"""


class AdminDashboardMapBuildingView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    View for Map Buildings.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        None
    """

    def get(self, request, *args, **kwargs):
        obj = Building.objects.actives()

        context = {
            "page_title": f"Building Map",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "objects": obj,
        }

        return render(request, "map/buildings.html", context)


class AdminDashboardMapIncidentView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    View for Map Incident.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        None
    """

    def get(self, request, *args, **kwargs):
        obj = Building.objects.all().values('name', 'latitude', 'longitude').annotate(
            count=Count('incident_building'))

        context = {
            "page_title": f"Incident Heat Map",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "objects": obj,
        }

        return render(request, "map/incidents.html", context)


class AdminDashboardMapFireProneAreaView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    View for Map Fire Prone Areas.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        None
    """

    def get(self, request, *args, **kwargs):
        obj = Building.objects.all()

        context = {
            "page_title": f"Fire Prone Areas",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "objects": obj,
        }

        return render(request, "map/fire_prone_area.html", context)