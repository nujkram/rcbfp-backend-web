from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from accounts.mixins.user_type_mixins import IsUserViewMixin
from inspections.constants import PENDING
from inspections.models import InspectionSchedule as Master

"""
URLS
# Inspection

from inspector_dashboards.controllers.views.inspector_dashboards.inspection import main as inspection_views

urlpatterns += {
    path(
        'inspection/list',
        inspection_views.InspectorDashboardInspectionListView.as_view(),
        name='inspector_dashboard_inspection_list'
    ),
    path(
        'inspection/<pk>/detail',
        inspection_views.InspectorDashboardInspectionDetailView.as_view(),
        name='inspector_dashboard_inspection_detail'
    ),
    path(
        'inspection/<pk>/update',
        inspection_views.InspectorDashboardInspectionUpdateView.as_view(),
        name='inspector_dashboard_inspection_update'
    ),
}
"""


class InspectorDashboardInspectionListView(LoginRequiredMixin, IsUserViewMixin, View):
    """
    List view for inspections.

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
        obj_list = Master.objects.filter(user=request.user, status=PENDING)
        paginator = Paginator(obj_list, 200)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Inspections List",
            "menu_section": "user_dashboards",
            "menu_subsection": "user_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "inspector_dashboard/inspection/list.html", context)


class InspectorDashboardInspectionDetailView(LoginRequiredMixin, IsUserViewMixin, View):
    """
    Create view for inspections.

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
            "page_title": f"inspection: {obj}",
            "menu_section": "user_dashboards",
            "menu_subsection": "user_dashboards",
            "menu_action": "detail",
            "obj": obj,
        }

        return render(request, "inspector_dashboard/inspection/detail.html", context)

