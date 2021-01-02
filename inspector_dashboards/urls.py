from django.urls import path

from inspector_dashboards.controllers.views.inspector_dashboards.home import main as home_views

version = 'api/v1'

READ_ONLY = {
    'get': 'list'
}

urlpatterns = [
    path(
        '',
        home_views.InspectorDashboardHomeView.as_view(),
        name='inspector_dashboard_home_view'
    ),
    path(
        'profile',
        home_views.InspectorDashboardProfileView.as_view(),
        name='inspector_dashboard_profile_view'
    ),
    path(
        'profile/update',
        home_views.InspectorDashboardUserUpdateView.as_view(),
        name='inspector_dashboard_update_profile_view'
    ),
]

# Inspection

from inspector_dashboards.controllers.views.inspector_dashboards.inspection import main as inspection_views

urlpatterns += {
    path(
        'inspection/list',
        inspection_views.InspectorDashboardInspectionListView.as_view(),
        name='inspector_dashboard_inspection_list'
    ),
    path(
        'inspection/<pk>/detail',
        inspection_views.InspectorDashboardInspectionDetailView.as_view(),
        name='inspector_dashboard_inspection_detail'
    ),
}

# Checklist

from inspector_dashboards.controllers.views.inspector_dashboards.checklist import main as checklist_views

urlpatterns += {
    path(
        'checklist/list',
        checklist_views.InspectorDashboardChecklistListView.as_view(),
        name='inspector_dashboard_checklist_list'
    ),
    path(
        'checklist/<pk>/detail',
        checklist_views.InspectorDashboardChecklistDetailView.as_view(),
        name='inspector_dashboard_checklist_detail'
    ),
    path(
        'checklist/create/<pk>',
        checklist_views.InspectorDashboardChecklistCreateView.as_view(),
        name='inspector_dashboard_checklist_create'
    ),
    path(
        'checklist/<pk>/update',
        checklist_views.InspectorDashboardChecklistUpdateView.as_view(),
        name='inspector_dashboard_checklist_update'
    ),
    path(
        'checklist/<pk>/delete',
        checklist_views.InspectorDashboardChecklistDeleteView.as_view(),
        name='inspector_dashboard_checklist_delete'
    )
}
