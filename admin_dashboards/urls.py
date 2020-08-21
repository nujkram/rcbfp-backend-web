from django.urls import path
from django.views.generic import TemplateView

from admin_dashboards.controllers.views.admin_dashboards.home import main as home_views

urlpatterns = [
    path(
        '',
        home_views.AdminDashboardHomeView.as_view(),
        name='admin_dashboard_home_view'
    ),
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

# Incident

from admin_dashboards.controllers.views.admin_dashboards.incident import main as incident_views

urlpatterns += {
    path(
        'incident/list',
        incident_views.AdminDashboardIncidentListView.as_view(),
        name='admin_dashboard_incident_list'
    ),
    path(
        'incident/<pk>/detail',
        incident_views.AdminDashboardIncidentDetailView.as_view(),
        name='admin_dashboard_incident_detail'
    ),
    path(
        'incident/create',
        incident_views.AdminDashboardIncidentCreateView.as_view(),
        name='admin_dashboard_incident_create'
    ),
    path(
        'incident/<pk>/update',
        incident_views.AdminDashboardIncidentUpdateView.as_view(),
        name='admin_dashboard_incident_update'
    ),
    path(
        'incident/<pk>/delete',
        incident_views.AdminDashboardIncidentDeleteView.as_view(),
        name='admin_dashboard_incident_delete'
    )
}

# Business Application

from admin_dashboards.controllers.views.admin_dashboards.business_application import main as business_application_views

urlpatterns += {
    path(
        'business_application/list',
        business_application_views.AdminDashboardBusinessApplicationListView.as_view(),
        name='admin_dashboard_business_application_list'
    ),
    path(
        'business_application/<pk>/detail',
        business_application_views.AdminDashboardBusinessApplicationDetailView.as_view(),
        name='admin_dashboard_business_application_detail'
    ),
    path(
        'business_application/create',
        business_application_views.AdminDashboardBusinessApplicationCreateView.as_view(),
        name='admin_dashboard_business_application_create'
    ),
    path(
        'business_application/<pk>/update',
        business_application_views.AdminDashboardBusinessApplicationUpdateView.as_view(),
        name='admin_dashboard_business_application_update'
    ),
    path(
        'business_application/<pk>/delete',
        business_application_views.AdminDashboardBusinessApplicationDeleteView.as_view(),
        name='admin_dashboard_business_application_delete'
    )
}

# Maps

from admin_dashboards.controllers.views.admin_dashboards.map import main as map_views

urlpatterns += {
    path(
        'map/buildings',
        map_views.AdminDashboardMapBuildingView.as_view(),
        name='admin_dashboard_map_building_view'
    ),
    path(
        'map/incidents',
        map_views.AdminDashboardMapIncidentView.as_view(),
        name='admin_dashboard_map_incident_view'
    ),
    path(
        'map/fire-prone',
        map_views.AdminDashboardMapFireProneAreaView.as_view(),
        name='admin_dashboard_map_fire_prone_area_view'
    ),
}

# Analytics

from .controllers.views.admin_dashboards.analytics.linear_regression import main as linear_regression_views
from .controllers.views.admin_dashboards.analytics.dtree import main as dtree_views

urlpatterns += {
    path(
        'analytics/linear_regression/run',
        linear_regression_views.AdminDashboardAnalyticsLinearRegressionFormView.as_view(),
        name='admin_dashboard_analytics_linear_regression_run_view'
    ),
    path(
        'analytics/decision_tree/run',
        dtree_views.AdminDashboardAnalyticsDecisionTreeFormView.as_view(),
        name='admin_dashboard_analytics_decision_tree_run_view'
    ),
}
