from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from incidents.models import Incident as Master
from admin_dashboards.controllers.views.admin_dashboards.incident.forms import IncidentForm as MasterForm


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
        paginator = Paginator(obj_list, 50)
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
        context = {
            "page_title": "Create new Incident",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "form": form
        }

        return render(request, "incident/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        if form.is_valid():
            data = form.save(commit=False)
            data.created_by = request.user
            data.save()
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
                "page_title": "Create new Incident",
                "menu_section": "admin_dashboards",
                "menu_subsection": "admin_dashboards",
                "menu_action": "create",
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "incident/form.html", context)


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
        obj = get_object_or_404(Master, pk= kwargs.get('pk', None))
        context = {
            "page_title": f"Incident: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj
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
        obj = get_object_or_404(Master, pk = kwargs.get('pk', None))
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
        obj = get_object_or_404(Master, pk = kwargs.get('pk', None))
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
        obj = get_object_or_404(Master, pk = kwargs.get('pk', None))
        context = {
            "page_title": f"Delete Incident: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "incident/delete.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk = kwargs.get('pk', None))

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