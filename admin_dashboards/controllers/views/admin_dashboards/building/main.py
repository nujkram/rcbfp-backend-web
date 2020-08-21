from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator

from accounts.mixins.user_type_mixins import IsAdminViewMixin

from buildings.models.building.building_models import Building as Master
from admin_dashboards.controllers.views.admin_dashboards.building.forms import BuildingForm as MasterForm
from locations.models import Region, Province, City

"""
URLS
# Building

from admin_dashboards.controllers.views.admin_dashboards.building import main as building_views

urlpatterns += {
    path(
        'building/list',
        building_views.AdminDashboardBuildingListView.as_view(),
        name='admin_dashboard_building_list'
    ),
    path(
        'building/<pk>/detail',
        building_views.AdminDashboardBuildingDetailView.as_view(),
        name='admin_dashboard_building_detail'
    ),
    path(
        'building/create',
        building_views.AdminDashboardBuildingCreateView.as_view(),
        name='admin_dashboard_building_create'
    ),
    path(
        'building/<pk>/update',
        building_views.AdminDashboardBuildingUpdateView.as_view(),
        name='admin_dashboard_building_update'
    ),
    path(
        'building/<pk>/delete',
        building_views.AdminDashboardBuildingDeleteView.as_view(),
        name='admin_dashboard_building_delete'
    )
}
"""


class AdminDashboardBuildingListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Buildings.

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
        paginator = Paginator(obj_list, 50)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Buildings",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "building/list.html", context)


class AdminDashboardBuildingCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
        regions = Region.objects.all()
        provinces = Province.objects.all()
        cities = City.objects.all()

        if 'building_formdata' in request.session:
            building_formdata = request.session['building_formdata']
            del request.session['building_formdata']
        else:
            building_formdata = {
                'name': '',
                'address': '',
                'latitude': '',
                'longitude': '',
                'date_of_construction': '',
                'floor_number': '',
                'height': '',
                'floor_area': '',
                'total_floor_area': '',
                'beams': '',
                'columns': '',
                'flooring': '',
                'exterior_walls': '',
                'corridor_walls': '',
                'room_partitions': '',
                'main_stair': '',
                'window': '',
                'ceiling': '',
                'main_door': '',
                'trusses': '',
                'roof': '',
                'entry_road_width': '',
                'region': '',
                'province': '',
                'city': '',
            }

        context = {
            "page_title": "Create new Building",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "building_formdata": building_formdata,
            "form": form,
            'regions': regions,
            'provinces': provinces,
            'cities': cities,
        }

        return render(request, "building/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(data=request.POST)

        building_formdata = {
            'name': request.POST.get('name', ''),
            'address': request.POST.get('address', ''),
            'latitude': request.POST.get('latitude', ''),
            'longitude': request.POST.get('longitude', ''),
            'date_of_construction': request.POST.get('date_of_construction', ''),
            'floor_number': request.POST.get('floor_number', ''),
            'height': request.POST.get('height', ''),
            'floor_area': request.POST.get('floor_area', ''),
            'total_floor_area': request.POST.get('total_floor_area', ''),
            'beams': request.POST.get('beams', ''),
            'columns': request.POST.get('columns', ''),
            'flooring': request.POST.get('flooring', ''),
            'exterior_walls': request.POST.get('exterior_walls', ''),
            'corridor_walls': request.POST.get('corridor_walls', ''),
            'room_partitions': request.POST.get('room_partitions', ''),
            'main_stair': request.POST.get('main_stair', ''),
            'window': request.POST.get('window', ''),
            'ceiling': request.POST.get('ceiling', ''),
            'main_door': request.POST.get('main_door', ''),
            'trusses': request.POST.get('trusses', ''),
            'roof': request.POST.get('roof', ''),
            'entry_road_width': request.POST.get('entry_road_width', ''),
            'region': request.POST.get('region', ''),
            'province': request.POST.get('province', ''),
            'city': request.POST.get('city', ''),
        }

        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            latitude = form.cleaned_data['latitude']
            longitude = form.cleaned_data['longitude']
            date_of_construction = form.cleaned_data['date_of_construction']
            floor_number = form.cleaned_data['floor_number']
            height = form.cleaned_data['height']
            floor_area = form.cleaned_data['floor_area']
            total_floor_area = form.cleaned_data['total_floor_area']
            beams = form.cleaned_data['beams']
            columns = form.cleaned_data['columns']
            flooring = form.cleaned_data['flooring']
            exterior_walls = form.cleaned_data['exterior_walls']
            corridor_walls = form.cleaned_data['corridor_walls']
            room_partitions = form.cleaned_data['room_partitions']
            main_stair = form.cleaned_data['main_stair']
            window = form.cleaned_data['window']
            ceiling = form.cleaned_data['ceiling']
            main_door = form.cleaned_data['main_door']
            trusses = form.cleaned_data['trusses']
            roof = form.cleaned_data['roof']
            entry_road_width = form.cleaned_data['entry_road_width']
            region = form.cleaned_data['region']
            province = form.cleaned_data['province']
            city = form.cleaned_data['city']

            building, building_message = Master.objects.create(
                name=name,
                address=address,
                latitude=latitude,
                longitude=longitude,
                date_of_construction=date_of_construction,
                floor_number=floor_number,
                height=height,
                floor_area=floor_area,
                total_floor_area=total_floor_area,
                beams=beams,
                columns=columns,
                flooring=flooring,
                exterior_walls=exterior_walls,
                corridor_walls=corridor_walls,
                room_partitions=room_partitions,
                main_stair=main_stair,
                window=window,
                ceiling=ceiling,
                main_door=main_door,
                trusses=trusses,
                roof=roof,
                entry_road_width=entry_road_width,
                region=region,
                province=province,
                city=city
            )

            if building:
                messages.success(request, 'Building created!', extra_tags='success')
            else:
                messages.error(request, building_message, extra_tags='danger')
        else:
            messages.error(request, form.errors, extra_tags='danger')
            request.session['building_formdata'] = building_formdata

        return HttpResponseRedirect(reverse('admin_dashboard_building_create'))


class AdminDashboardBuildingDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
            "page_title": f"Building: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj
        }

        return render(request, "building/detail.html", context)


class AdminDashboardBuildingUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
            "page_title": f"Update Building: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form
        }

        return render(request, "building/form.html", context)

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
                    'admin_dashboard_building_detail',
                    kwargs={
                        'pk': data.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update Building: {obj}",
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
            return render(request, "building/form.html", context)


class AdminDashboardBuildingDeleteView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Buildings.

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
            "page_title": f"Delete Building: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "delete",
            "obj": obj
        }

        return render(request, "building/delete.html", context)

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
                'admin_dashboard_building_list'
            )
        )
