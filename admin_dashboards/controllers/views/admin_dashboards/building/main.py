from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from buildings.models.building.building_models import Building as Master
from admin_dashboards.controllers.views.admin_dashboards.building.forms import BuildingForm as MasterForm


"""
URLS
# Building

from admin_dashboards.controllers.views.admin_dashboards.building import main as building_views

urlpatterns += {
    path(
        'building/list',
        building_views.AdminDashboardBuildingListView.as_view(),
        name='admin_dashboard_building_list'
    ),
    path(
        'building/<pk>/detail',
        building_views.AdminDashboardBuildingDetailView.as_view(),
        name='admin_dashboard_building_detail'
    ),
    path(
        'building/create',
        building_views.AdminDashboardBuildingCreateView.as_view(),
        name='admin_dashboard_building_create'
    ),
    path(
        'building/<pk>/update',
        building_views.AdminDashboardBuildingUpdateView.as_view(),
        name='admin_dashboard_building_update'
    ),
    path(
        'building/<pk>/delete',
        building_views.AdminDashboardBuildingDeleteView.as_view(),
        name='admin_dashboard_building_delete'
    )
}
"""

class AdminDashboardBuildingListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Buildings.

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
            "page_title": f"Buildings",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "building/list.html", context)


class AdminDashboardBuildingCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
            "page_title": "Create new Building",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "form": form
        }

        return render(request, "building/form.html", context)

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
                    'admin_dashboard_building_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Building",
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
            return render(request, "building/form.html", context)


class AdminDashboardBuildingDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
            "page_title": f"Building: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "building/detail.html", context)


class AdminDashboardBuildingUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
            "page_title": "Update Building: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "admin_dashboard/form.html", context)

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
                    'admin_dashboard_building_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Update Building: {obj}",
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
            return render(request, "building/form.html", context)


class AdminDashboardBuildingDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
            "page_title": "Delete Building: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "building/delete.html", context)

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
                'admin_dashboard_building_list'
            )
        )