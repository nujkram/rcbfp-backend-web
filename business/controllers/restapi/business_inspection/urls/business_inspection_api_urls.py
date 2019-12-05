from django.urls import path

from business.controllers.restapi.business_inspection import business_inspection_api as apiview

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
        f'{version}/public/business/business_inspection/list',
        apiview.ApiPublicBusinessInspectionListDetail.as_view(READ_ONLY),
        name='api_public_business_business_inspection_list'
    ),

    # private
    path(
        f'{version}/private/business/business_inspection/create',
        apiview.ApiPrivateBusinessInspectionViewSet.as_view(CREATE),
        name='api_private_business_business_inspection_create'
    ),
    path(
        f'{version}/private/business/business_inspection/<pk>/update',
        apiview.ApiPrivateBusinessInspectionViewSet.as_view(UPDATE),
        name='api_private_business_business_inspection_update'
    ),
    path(
        f'{version}/private/business/business_inspection/<pk>/delete',
        apiview.ApiPrivateBusinessInspectionViewSet.as_view(DELETE),
        name='api_private_business_business_inspection_delete'
    ),
]