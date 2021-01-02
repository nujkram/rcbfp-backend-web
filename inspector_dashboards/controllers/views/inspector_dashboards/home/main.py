from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsUserViewMixin
from accounts.models import Account
from inspections.constants import PENDING
from inspections.models import InspectionSchedule as Master
from inspector_dashboards.controllers.views.inspector_dashboards.home.forms import UserForm as MasterForm


class InspectorDashboardHomeView(LoginRequiredMixin, IsUserViewMixin, View):
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


class InspectorDashboardProfileView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        profile = request.user.profile
        context = {
            'page_title': f'{profile} profile',
            'profile': profile
        }

        return render(request, 'inspector_dashboard/profile/detail.html', context)


class InspectorDashboardUserUpdateView(LoginRequiredMixin, IsUserViewMixin, View):
    """
    Update view for User.

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
        obj = request.user
        form = MasterForm(instance=obj)
        context = {
            "page_title": f"Update User: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form,
        }

        return render(request, "inspector_dashboard/profile/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = request.user
        print(obj.pk)
        form = MasterForm(request.POST, instance=obj)

        if form.is_valid():
            password = form.cleaned_data['password1']

            user = Account.objects.get(pk=obj.pk)
            user.set_password(password)

            user.save()

            messages.success(
                request,
                f'{obj} updated! Please re-login to continue',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'root'
                )
            )
        else:
            context = {
                "page_title": f"Update User: {obj}",
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
            return render(request, "inspector_dashboard/profile/form.html", context)