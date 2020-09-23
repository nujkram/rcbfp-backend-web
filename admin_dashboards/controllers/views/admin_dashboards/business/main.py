from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from admin_dashboards.controllers.views.admin_dashboards.business.forms import BusinessForm as MasterForm
from buildings.models.building.building_models import Building
from business.models import Business as Master
from checklists.models.checklist.checklist_models import Checklist
from locations.models import Region, Province, City

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
        for obj in obj_list:
            if obj.business_checklists:
                obj.is_safe()
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
        buildings = Building.objects.all()
        default_region = Region.objects.get(pk=6)  # Region VI
        default_province = Province.objects.get(pk=22)  # Capiz
        default_city = City.objects.get(pk=381)  # Roxas City
        regions = Region.objects.all()
        provinces = Province.objects.filter(region=default_region)
        cities = City.objects.filter(province=default_province)
        context = {
            "page_title": "Create new Business",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "form": form,
            "buildings": buildings,
            "regions": regions,
            "provinces": provinces,
            "cities": cities,
            "default_region": default_region,
            "default_province": default_province,
            "default_city": default_city,
        }

        return render(request, "business/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        business_formdata = {
            'name': request.POST.get('name', ''),
            'nature': request.POST.get('nature', ''),
            'owner_first_name': request.POST.get('owner_first_name', ''),
            'owner_middle_name': request.POST.get('owner_middle_name', ''),
            'owner_last_name': request.POST.get('owner_last_name', ''),
            'address': request.POST.get('address', ''),
            'landline': request.POST.get('landline', ''),
            'mobile_number': request.POST.get('mobile_number', ''),
            'email': request.POST.get('email', ''),
            'building': request.POST.get('building', ''),
            'region': request.POST.get('region', ''),
            'province': request.POST.get('province', ''),
            'city': request.POST.get('city', ''),
        }

        if form.is_valid():
            name = form.cleaned_data['name']
            nature = form.cleaned_data['nature']
            owner_first_name = form.cleaned_data['owner_first_name']
            owner_middle_name = form.cleaned_data['owner_middle_name']
            owner_last_name = form.cleaned_data['owner_last_name']
            address = form.cleaned_data['address']
            landline = form.cleaned_data['landline']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            building = form.cleaned_data['building']
            region = form.cleaned_data['region']
            province = form.cleaned_data['province']
            city = form.cleaned_data['city']

            business, building_message = Master.objects.create(
                name=name,
                nature=nature,
                owner_first_name=owner_first_name,
                owner_middle_name=owner_middle_name,
                owner_last_name=owner_last_name,
                address=address,
                landline=landline,
                mobile_number=mobile_number,
                email=email,
                building=building,
                region=region,
                province=province,
                city=city
            )

            if business:
                messages.success(request, 'Business created!', extra_tags='success')
                return HttpResponseRedirect(reverse('admin_dashboard_inspection_create_new',
                                                    kwargs={'building': building.pk, 'business': business.pk}))
            else:
                messages.error(request, building_message, extra_tags='danger')
                request.session['business_formdata'] = business_formdata
        else:
            messages.error(request, form.errors, extra_tags='danger')
            request.session['business_formdata'] = business_formdata

        return HttpResponseRedirect(reverse('admin_dashboard_business_create'))


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
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        checklists = Checklist.objects.filter(business=obj).order_by('-created')
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
    Update view for Businesss.

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
        buildings = Building.objects.all()
        form = MasterForm(initial=obj)
        default_region = Region.objects.get(pk=6)  # Region VI
        default_province = Province.objects.get(pk=22)  # Capiz
        default_city = City.objects.get(pk=381)  # Roxas City
        regions = Region.objects.all()
        provinces = Province.objects.filter(region=default_region)
        cities = City.objects.filter(province=default_province)

        context = {
            "page_title": f"Update Business: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form,
            "buildings": buildings,
            "regions": regions,
            "provinces": provinces,
            "cities": cities,
            "default_region": default_region,
            "default_province": default_province,
            "default_city": default_city,
        }

        return render(request, "business/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        form = MasterForm(request.POST, initial=obj)

        if form.is_valid():
            name = form.cleaned_data['name']
            nature = form.cleaned_data['nature']
            owner_first_name = form.cleaned_data['owner_first_name']
            owner_middle_name = form.cleaned_data['owner_middle_name']
            owner_last_name = form.cleaned_data['owner_last_name']
            address = form.cleaned_data['address']
            landline = form.cleaned_data['landline']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            building = form.cleaned_data['building']
            region = form.cleaned_data['region']
            province = form.cleaned_data['province']
            city = form.cleaned_data['city']

            Master.objects.filter(pk=obj.pk).update(
                name=name,
                nature=nature,
                owner_first_name=owner_first_name,
                owner_middle_name=owner_middle_name,
                owner_last_name=owner_last_name,
                address=address,
                landline=landline,
                mobile_number=mobile_number,
                email=email,
                building=building,
                region=region,
                province=province,
                city=city,
            )

            messages.success(
                request,
                f'{obj} updated!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'admin_dashboard_business_detail',
                    kwargs={
                        'pk': obj.pk
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
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        context = {
            "page_title": f"Delete Business: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "business/delete.html", context)

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
                'admin_dashboard_business_list'
            )
        )


class AdminDashboardBusinessCreateByBuildingView(LoginRequiredMixin, IsAdminViewMixin, View):
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
        building = get_object_or_404(Building, pk=kwargs.get('pk', None))
        buildings = Building.objects.all()
        default_region = Region.objects.get(pk=6)  # Region VI
        default_province = Province.objects.get(pk=22)  # Capiz
        default_city = City.objects.get(pk=381)  # Roxas City
        regions = Region.objects.all()
        provinces = Province.objects.filter(region=default_region)
        cities = City.objects.filter(province=default_province)
        context = {
            "page_title": "Create new Business",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "form": form,
            "building": building,
            "buildings": buildings,
            "regions": regions,
            "provinces": provinces,
            "cities": cities,
            "default_region": default_region,
            "default_province": default_province,
            "default_city": default_city,
        }

        return render(request, "business/new_business.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        business_formdata = {
            'name': request.POST.get('name', ''),
            'nature': request.POST.get('nature', ''),
            'owner_first_name': request.POST.get('owner_first_name', ''),
            'owner_middle_name': request.POST.get('owner_middle_name', ''),
            'owner_last_name': request.POST.get('owner_last_name', ''),
            'address': request.POST.get('address', ''),
            'landline': request.POST.get('landline', ''),
            'mobile_number': request.POST.get('mobile_number', ''),
            'email': request.POST.get('email', ''),
            'building': request.POST.get('building', ''),
            'region': request.POST.get('region', ''),
            'province': request.POST.get('province', ''),
            'city': request.POST.get('city', ''),
        }

        if form.is_valid():
            name = form.cleaned_data['name']
            nature = form.cleaned_data['nature']
            owner_first_name = form.cleaned_data['owner_first_name']
            owner_middle_name = form.cleaned_data['owner_middle_name']
            owner_last_name = form.cleaned_data['owner_last_name']
            address = form.cleaned_data['address']
            landline = form.cleaned_data['landline']
            mobile_number = form.cleaned_data['mobile_number']
            email = form.cleaned_data['email']
            building = form.cleaned_data['building']
            region = form.cleaned_data['region']
            province = form.cleaned_data['province']
            city = form.cleaned_data['city']

            business, building_message = Master.objects.create(
                name=name,
                nature=nature,
                owner_first_name=owner_first_name,
                owner_middle_name=owner_middle_name,
                owner_last_name=owner_last_name,
                address=address,
                landline=landline,
                mobile_number=mobile_number,
                email=email,
                building=building,
                region=region,
                province=province,
                city=city
            )

            if business:
                messages.success(request, 'Business created!', extra_tags='success')
                return HttpResponseRedirect(reverse('admin_dashboard_inspection_create_new',
                                                    kwargs={'building': building.pk, 'business': business.pk}))
            else:
                messages.error(request, building_message, extra_tags='danger')
                request.session['business_formdata'] = business_formdata
        else:
            messages.error(request, form.errors, extra_tags='danger')
            request.session['business_formdata'] = business_formdata

        return HttpResponseRedirect(reverse('admin_dashboard_business_create'))
