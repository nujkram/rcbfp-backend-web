from django.urls import path

from business.controllers.restapi.business import business_api as apiview

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
        f'{version}/public/business/business/list',
        apiview.ApiPublicBusinessListDetail.as_view(READ_ONLY),
        name='api_public_business_business_list'
    ),

    # private
    path(
        f'{version}/private/business/business/create',
        apiview.ApiPrivateBusinessViewSet.as_view(CREATE),
        name='api_private_business_business_create'
    ),
    path(
        f'{version}/private/business/business/<pk>/update',
        apiview.ApiPrivateBusinessViewSet.as_view(UPDATE),
        name='api_private_business_business_update'
    ),
    path(
        f'{version}/private/business/business/<pk>/delete',
        apiview.ApiPrivateBusinessViewSet.as_view(DELETE),
        name='api_private_business_business_delete'
    ),
]