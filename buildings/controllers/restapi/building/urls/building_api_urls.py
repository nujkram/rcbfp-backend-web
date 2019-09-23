from django.urls import path

from buildings.controllers.restapi.building import building_api as apiview

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
        f'{version}/public/buildings/building/list',
        apiview.ApiPublicBuildingListDetail.as_view(READ_ONLY),
        name='api_public_buildings_building_list'
    ),

    # private
    path(
        f'{version}/private/buildings/building/create',
        apiview.ApiPrivateBuildingViewSet.as_view(CREATE),
        name='api_private_buildings_building_create'
    ),
    path(
        f'{version}/private/buildings/building/<pk>/update',
        apiview.ApiPrivateBuildingViewSet.as_view(UPDATE),
        name='api_private_buildings_building_update'
    ),
    path(
        f'{version}/private/buildings/building/<pk>/delete',
        apiview.ApiPrivateBuildingViewSet.as_view(DELETE),
        name='api_private_buildings_building_delete'
    ),
]