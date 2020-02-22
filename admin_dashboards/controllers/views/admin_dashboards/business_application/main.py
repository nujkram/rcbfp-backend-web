from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from business.models.business_application.business_application_model import BusinessApplication as Master
from admin_dashboards.controllers.views.admin_dashboards.business_application.forms import BusinessApplicationForm as MasterForm


"""
URLS
# Business Application

from admin_dashboards.controllers.views.admin_dashboards.business_application import main as business_application_views

urlpatterns += {
    path(
        'business_application/list',
        business_application_views.AdminDashboardBusinessApplicationListView.as_view(),
        name='admin_dashboard_business_application_list'
    ),
    path(
        'business_application/<pk>/detail',
        business_application_views.AdminDashboardBusinessApplicationDetailView.as_view(),
        name='admin_dashboard_business_application_detail'
    ),
    path(
        'business_application/create',
        business_application_views.AdminDashboardBusinessApplicationCreateView.as_view(),
        name='admin_dashboard_business_application_create'
    ),
    path(
        'business_application/<pk>/update',
        business_application_views.AdminDashboardBusinessApplicationUpdateView.as_view(),
        name='admin_dashboard_business_application_update'
    ),
    path(
        'business_application/<pk>/delete',
        business_application_views.AdminDashboardBusinessApplicationDeleteView.as_view(),
        name='admin_dashboard_business_application_delete'
    )
}
"""

class AdminDashboardBusinessApplicationListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Business Applications.

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
        obj_list = Master.objects.filter(business=kwargs.get('pk', None))
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Business Applications",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "business_application/list.html", context)


class AdminDashboardBusinessApplicationCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Business Applications.

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
            "page_title": "Create new Business Application",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "form": form
        }

        return render(request, "business_application/form.html", context)

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
                    'admin_dashboard_business_application_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Business Application",
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
            return render(request, "business_application/form.html", context)


class AdminDashboardBusinessApplicationDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Business Applications.

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
            "page_title": f"Business Application: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "business_application/detail.html", context)


class AdminDashboardBusinessApplicationUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Business Applications.

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
            "page_title": f"Update Business Application: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "business_application/form.html", context)

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
                    'admin_dashboard_business_application_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update Business Application: {obj}",
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
            return render(request, "business_application/form.html", context)


class AdminDashboardBusinessApplicationDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Business Applications.

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
            "page_title": f"Delete Business Application: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "business_application/delete.html", context)

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
                'admin_dashboard_business_application_list'
            )
        )