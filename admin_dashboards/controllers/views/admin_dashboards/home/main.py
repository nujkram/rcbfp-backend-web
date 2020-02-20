from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views import View

from accounts.mixins.user_type_mixins import IsAdminAPIMixin
from accounts.models import Account
from accounts.constants import USER


class AdminDashboardHomeView(LoginRequiredMixin, IsAdminAPIMixin, View):
    def get(self, request, *args, **kwargs):

        context = {
            "page_title": f"RCBFP: Admin Dashboard",
            "menu_section": "home",
            "menu_subsection": "home",
            "menu_action": "list",
        }

        return render(request, 'home/main.html', context)