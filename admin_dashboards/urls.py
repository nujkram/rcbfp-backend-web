from django.urls import path

from admin_dashboards.controllers.views.admin_dashboards.home import main as home_views

urlpatterns = [
    path(
        '',
        home_views.AdminDashboardHomeView.as_view(),
        name='admin_dashboard_home_view'
    )
]

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