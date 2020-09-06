from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View
from datetime import date

from accounts.mixins.user_type_mixins import IsAdminAPIMixin
from accounts.models import Account
from accounts.constants import USER
from checklists.constants import NOT_TO_OPERATE, REINSPECT
from checklists.models.checklist.checklist_models import Checklist
from inspections.constants import PENDING
from inspections.models import InspectionSchedule


class AdminDashboardHomeView(LoginRequiredMixin, IsAdminAPIMixin, View):
    def get(self, request, *args, **kwargs):
        now = date.today()
        inspection_schedules = InspectionSchedule.objects.filter(status=PENDING)
        
        checklist_current_year = Checklist.objects.filter(remarks__in=(NOT_TO_OPERATE, REINSPECT), date_checked__year=now.year)

        context = {
            "page_title": f"RCBFP: Admin Dashboard",
            "menu_section": "home",
            "menu_subsection": "home",
            "menu_action": "list",
            "inspection_schedules": inspection_schedules,
            "checklist_current_year": checklist_current_year,
        }

        return render(request, 'home/main.html', context)
