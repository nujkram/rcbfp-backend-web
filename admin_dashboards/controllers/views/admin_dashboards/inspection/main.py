from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.constants import USER
from accounts.mixins.user_type_mixins import IsAdminViewMixin
from accounts.models import Account
from buildings.models.building.building_models import Building
from business.models import Business

from inspections.models import InspectionSchedule as Master
from admin_dashboards.controllers.views.admin_dashboards.inspection.forms import InspectionForm as MasterForm

"""
URLS
# Inspection

from admin_dashboards.controllers.views.admin_dashboards.inspection import main as inspection_views

urlpatterns += {
    path(
        'inspection/list',
        inspection_views.AdminDashboardInspectionListView.as_view(),
        name='admin_dashboard_inspection_list'
    ),
    path(
        'inspection/<pk>/detail',
        inspection_views.AdminDashboardInspectionDetailView.as_view(),
        name='admin_dashboard_inspection_detail'
    ),
    path(
        'inspection/create',
        inspection_views.AdminDashboardInspectionCreateView.as_view(),
        name='admin_dashboard_inspection_create'
    ),
    path(
        'inspection/<pk>/update',
        inspection_views.AdminDashboardInspectionUpdateView.as_view(),
        name='admin_dashboard_inspection_update'
    ),
    path(
        'inspection/<pk>/delete',
        inspection_views.AdminDashboardInspectionDeleteView.as_view(),
        name='admin_dashboard_inspection_delete'
    )
}
"""


class AdminDashboardInspectionListView(LoginRequiredMixin, IsAdminViewMixin, View):
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
        obj_list = Master.objects.actives()
        paginator = Paginator(obj_list, 200)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"inspections",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "inspection/list.html", context)


class AdminDashboardInspectionCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for inspections.

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
        buildings = Building.objects.all()
        businesses = Business.objects.all()
        users = Account.objects.filter(user_type=USER)
        
        if 'inspection_formdata' in request.session:
            inspection_formdata = request.session['inspection_formdata']
            del request.session['inspection_formdata']
        else:
            inspection_formdata = {
                'inspection_date': '',
                'user': '',
                'building': '',
                'business': '',
            }
        
        context = {
            "page_title": "Create new inspection",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "inspection_formdata": inspection_formdata,
            "form": form,
            "buildings": buildings,
            "businesses": businesses,
            "users": users,

        }

        return render(request, "inspection/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        inspection_formdata = {
            'inspection_date': request.POST.get('inspection_date', ''),
            'user': request.POST.get('user', ''),
            'building': request.POST.get('building', ''),
            'business': request.POST.get('business', ''),
        }

        if form.is_valid():
            inspection_date = form.cleaned_data['inspection_date'],
            user = form.cleaned_data['user'],
            building = form.cleaned_data['building'],
            business = form.cleaned_data['business'],

            inspection, inspection_message = Master.objects.create(
                inspection_date=inspection_date,
                user=user,
                building=building,
                business=business,
            )

            if inspection:
                messages.success(request, 'Inspection created!', extra_tags='success')
                return HttpResponseRedirect(reverse('admin_dashboard_inspection_detail', kwargs={'pk': inspection.pk}))
            else:
                messages.error(request, inspection_message, extra_tags='danger')
                request.session['inspection_formdata'] = inspection_formdata
        else:
            messages.error(request, form.errors, extra_tags='danger')
            request.session['inspection_formdata'] = inspection_formdata

        return HttpResponseRedirect(reverse('admin_dashboard_inspection_create'))


class AdminDashboardInspectionDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
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
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj,
        }

        return render(request, "inspection/detail.html", context)


class AdminDashboardInspectionUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Update view for inspections.

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
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        form = MasterForm(instance=obj)

        context = {
            "page_title": f"Update inspection: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "inspection/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
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
                    'admin_dashboard_inspection_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update inspection: {obj}",
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
            return render(request, "inspection/form.html", context)


class AdminDashboardInspectionDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for inspections.

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
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        context = {
            "page_title": f"Delete inspection: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "inspection/delete.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))

        messages.success(
            request,
            f'{obj} deleted!',
            extra_tags='success'
        )

        obj.delete()

        return HttpResponseRedirect(
            reverse(
                'admin_dashboard_inspection_list'
            )
        )
