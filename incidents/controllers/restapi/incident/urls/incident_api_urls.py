from django.urls import path

from incidents.controllers.restapi.incident import incident_api as apiview

version = 'api/v1'

###############################################################################
# Public
###############################################################################


READ_ONLY = {
  'get': 'list'
}

DETAIL = {
  'get': 'retrieve'
}

CREATE = {
  'get': 'list',
  'post': 'create',
}

UPDATE = {
  'get': 'retrieve',
  'put': 'update',
}

DELETE = {
  'get': 'retrieve',
  'delete': 'destroy',
}

urlpatterns = [
    # public
    path(
        f'{version}/public/incidents/incident/list',
        apiview.ApiPublicIncidentListDetail.as_view(READ_ONLY),
        name='api_public_incidents_incident_list'
    ),

    # private
    path(
        f'{version}/private/incidents/incident/create',
        apiview.ApiPrivateIncidentViewSet.as_view(CREATE),
        name='api_private_incidents_incident_create'
    ),
    path(
        f'{version}/private/incidents/incident/<pk>/update',
        apiview.ApiPrivateIncidentViewSet.as_view(UPDATE),
        name='api_private_incidents_incident_update'
    ),
    path(
        f'{version}/private/incidents/incident/<pk>/delete',
        apiview.ApiPrivateIncidentViewSet.as_view(DELETE),
        name='api_private_incidents_incident_delete'
    ),
]