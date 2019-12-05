from django.urls import path

from business.controllers.restapi.business_application import business_application_api as apiview

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
        f'{version}/public/business/business_application/list',
        apiview.ApiPublicBusinessApplicationListDetail.as_view(READ_ONLY),
        name='api_public_business_business_application_list'
    ),

    # private
    path(
        f'{version}/private/business/business_application/create',
        apiview.ApiPrivateBusinessApplicationViewSet.as_view(CREATE),
        name='api_private_business_business_application_create'
    ),
    path(
        f'{version}/private/business/business_application/<pk>/update',
        apiview.ApiPrivateBusinessApplicationViewSet.as_view(UPDATE),
        name='api_private_business_business_application_update'
    ),
    path(
        f'{version}/private/business/business_application/<pk>/delete',
        apiview.ApiPrivateBusinessApplicationViewSet.as_view(DELETE),
        name='api_private_business_business_application_delete'
    ),
]