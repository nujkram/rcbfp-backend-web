from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from business.models import Business as Master
from admin_dashboards.controllers.views.admin_dashboards.business.forms import BusinessForm as MasterForm
from checklists.models.checklist.checklist_models import Checklist

"""
URLS
# Business

from admin_dashboards.controllers.views.admin_dashboards.business import main as business_views

urlpatterns += {
    path(
        'business/list',
        business_views.AdminDashboardBusinessListView.as_view(),
        name='admin_dashboard_business_list'
    ),
    path(
        'business/<pk>/detail',
        business_views.AdminDashboardBusinessDetailView.as_view(),
        name='admin_dashboard_business_detail'
    ),
    path(
        'business/create',
        business_views.AdminDashboardBusinessCreateView.as_view(),
        name='admin_dashboard_business_create'
    ),
    path(
        'business/<pk>/update',
        business_views.AdminDashboardBusinessUpdateView.as_view(),
        name='admin_dashboard_business_update'
    ),
    path(
        'business/<pk>/delete',
        business_views.AdminDashboardBusinessDeleteView.as_view(),
        name='admin_dashboard_business_delete'
    )
}
"""

class AdminDashboardBusinessListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Businesss.

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
        paginator = Paginator(obj_list, 200)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Businesss",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "business/list.html", context)


class AdminDashboardBusinessCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Businesss.

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
            "page_title": "Create new Business",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "form": form
        }

        return render(request, "business/form.html", context)

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
                    'admin_dashboard_business_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": "Create new Business",
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
            return render(request, "business/form.html", context)


class AdminDashboardBusinessDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Businesss.

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
        checklists = Checklist.objects.filter(business=obj).order_by('date_checked')
        context = {
            "page_title": f"Business: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj,
            "checklists": checklists,
        }

        return render(request, "business/detail.html", context)


class AdminDashboardBusinessUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Businesss.

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
            "page_title": f"Update Business: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "business/form.html", context)

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
                    'admin_dashboard_business_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update Business: {obj}",
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
            return render(request, "business/form.html", context)


class AdminDashboardBusinessDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Businesss.

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
            "page_title": f"Delete Business: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "business/delete.html", context)

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
                'admin_dashboard_business_list'
            )
        )