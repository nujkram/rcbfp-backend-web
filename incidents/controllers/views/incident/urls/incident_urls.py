from django.urls import path

from incidents.controllers.views.incident import incident_views as view

###############################################################################
# Views
###############################################################################

urlpatterns = [
    path(
        '<incidents>/incident/list',
        view.IncidentListView.as_view(),
        name='incident_list'
    ),
    path(
        '<incidents>/incident/create',
        view.IncidentCreateView.as_view(),
        name='incident_create'
    ),
    path(
        '<incidents>/incident/<pk>/update',
        view.IncidentUpdateView.as_view(),
        name='incident_update'
    ),
    path(
        '<incidents>/incident/<pk>/detail',
        view.IncidentDetailView.as_view(),
        name='incident_detail'
    ),
    path(
        '<incidents>/incident/<pk>/delete',
        view.IncidentDeleteView.as_view(),
        name='incident_delete'
    ),
]

