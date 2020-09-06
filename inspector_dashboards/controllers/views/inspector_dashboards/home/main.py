from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsUserViewMixin
from inspections.constants import PENDING
from inspections.models import InspectionSchedule as Master


class AdminDashboardHomeView(LoginRequiredMixin, IsUserViewMixin, View):
    def get(self, request, *args, **kwargs):
        obj_list = Master.objects.filter(user=request.user, status=PENDING)
        paginator = Paginator(obj_list, 200)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"RCBFP: Inspector Dashboard",
            "menu_section": "home",
            "menu_subsection": "home",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, 'inspector_dashboard/home/main.html', context)
