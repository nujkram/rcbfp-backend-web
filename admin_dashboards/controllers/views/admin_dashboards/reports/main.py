from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from business.models import Business as Master

"""
URLS
# reports

from admin_dashboards.controllers.views.admin_dashboards.reports import main as report_views

urlpatterns += {
    path(
        'report/business/list',
        report_views.AdminDashboardBusinessStatusView.as_view(),
        name='admin_dashboard_business_status_list'
    ),
}
"""


class AdminDashboardBusinessStatusView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Compliant and Non-Compliant Business.

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
        obj_list = Master.objects.actives().order_by('status')
        paginator = Paginator(obj_list, 200)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Business Report",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "reports/business/list.html", context)
