from django.urls import path

from business.controllers.restapi.business_evaluation import business_evaluation_api as apiview

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
        f'{version}/public/business/business_evaluation/list',
        apiview.ApiPublicBusinessEvaluationListDetail.as_view(READ_ONLY),
        name='api_public_business_business_evaluation_list'
    ),

    # private
    path(
        f'{version}/private/business/business_evaluation/create',
        apiview.ApiPrivateBusinessEvaluationViewSet.as_view(CREATE),
        name='api_private_business_business_evaluation_create'
    ),
    path(
        f'{version}/private/business/business_evaluation/<pk>/update',
        apiview.ApiPrivateBusinessEvaluationViewSet.as_view(UPDATE),
        name='api_private_business_business_evaluation_update'
    ),
    path(
        f'{version}/private/business/business_evaluation/<pk>/delete',
        apiview.ApiPrivateBusinessEvaluationViewSet.as_view(DELETE),
        name='api_private_business_business_evaluation_delete'
    ),
]