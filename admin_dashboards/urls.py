from django.urls import path
from django.views.generic import TemplateView

from admin_dashboards.controllers.views.admin_dashboards.home import main as home_views
from business.controllers.restapi.business.business_api import ApiBusinessesByBuilding

version = 'api/v1'

READ_ONLY = {
    'get': 'list'
}

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
        'building/create/new',
        building_views.AdminDashboardBuildingCreateNewView.as_view(),
        name='admin_dashboard_building_create_new'
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
        'business/<pk>/create',
        business_views.AdminDashboardBusinessCreateByBuildingView.as_view(),
        name='admin_dashboard_business_create_by_building'
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
    ),

    # API
    path(f'{version}/businesses_by_building', ApiBusinessesByBuilding.as_view(), name='businesses_by_building'),
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

# Maps

from admin_dashboards.controllers.views.admin_dashboards.map import main as map_views

urlpatterns += {
    path(
        'map/businesses',
        map_views.AdminDashboardMapBusinessView.as_view(),
        name='admin_dashboard_map_business_view'
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

# Checklist

from admin_dashboards.controllers.views.admin_dashboards.checklist import main as checklist_views

urlpatterns += {
    path(
        'checklist/list',
        checklist_views.AdminDashboardChecklistListView.as_view(),
        name='admin_dashboard_checklist_list'
    ),
    path(
        'checklist/<pk>/detail',
        checklist_views.AdminDashboardChecklistDetailView.as_view(),
        name='admin_dashboard_checklist_detail'
    ),
    path(
        'checklist/create',
        checklist_views.AdminDashboardChecklistCreateView.as_view(),
        name='admin_dashboard_checklist_create'
    ),
    path(
        'checklist/create/<pk>',
        checklist_views.AdminDashboardChecklistCreateView.as_view(),
        name='admin_dashboard_checklist_create_by_business'
    ),
    path(
        'checklist/<pk>/update',
        checklist_views.AdminDashboardChecklistUpdateView.as_view(),
        name='admin_dashboard_checklist_update'
    ),
    path(
        'checklist/<pk>/delete',
        checklist_views.AdminDashboardChecklistDeleteView.as_view(),
        name='admin_dashboard_checklist_delete'
    ),
    path(
        'checklist/<pk>/summary',
        checklist_views.AdminDashboardChecklistSummaryView.as_view(),
        name='admin_dashboard_checklist_summary'
    )
}

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
        'inspection/<building>/<business>/create',
        inspection_views.AdminDashboardInspectionCreateNewView.as_view(),
        name='admin_dashboard_inspection_create_new'
    ),
    path(
        'inspection/reinspect',
        inspection_views.AdminDashboardInspectionCreateReinspectView.as_view(),
        name='admin_dashboard_inspection_create_reinspect'
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

# User

from admin_dashboards.controllers.views.admin_dashboards.user import main as user_views

urlpatterns += {
    path(
        'user/list',
        user_views.AdminDashboardUserListView.as_view(),
        name='admin_dashboard_user_list'
    ),
    path(
        'user/<pk>/detail',
        user_views.AdminDashboardUserDetailView.as_view(),
        name='admin_dashboard_user_detail'
    ),
    path(
        'user/create',
        user_views.AdminDashboardUserCreateView.as_view(),
        name='admin_dashboard_user_create'
    ),
    path(
        'user/<pk>/update',
        user_views.AdminDashboardUserUpdateView.as_view(),
        name='admin_dashboard_user_update'
    ),
    path(
        'user/<pk>/change_password',
        user_views.AdminDashboardUserUpdatePasswordView.as_view(),
        name='admin_dashboard_user_update_password'
    ),

}

# reports

from admin_dashboards.controllers.views.admin_dashboards.reports import main as report_views

urlpatterns += {
    path(
        'report/business/list',
        report_views.AdminDashboardBusinessStatusView.as_view(),
        name='admin_dashboard_business_status_list'
    ),
    path(
        'report/analytics',
        report_views.AdminDashboardAnalyticsView.as_view(),
        name='admin_dashboard_analytics'
    ),
    path(
        'report/building/list',
        report_views.AdminDashboardBuildingStatusView.as_view(),
        name='admin_dashboard_building_status_list'
    ),
}
