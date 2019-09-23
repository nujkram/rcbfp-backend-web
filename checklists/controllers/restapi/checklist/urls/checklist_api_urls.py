from django.urls import path

from checklists.controllers.restapi.checklist import checklist_api as apiview

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
        f'{version}/public/checklists/checklist/list',
        apiview.ApiPublicChecklistListDetail.as_view(READ_ONLY),
        name='api_public_checklists_checklist_list'
    ),

    # private
    path(
        f'{version}/private/checklists/checklist/create',
        apiview.ApiPrivateChecklistViewSet.as_view(CREATE),
        name='api_private_checklists_checklist_create'
    ),
    path(
        f'{version}/private/checklists/checklist/<pk>/update',
        apiview.ApiPrivateChecklistViewSet.as_view(UPDATE),
        name='api_private_checklists_checklist_update'
    ),
    path(
        f'{version}/private/checklists/checklist/<pk>/delete',
        apiview.ApiPrivateChecklistViewSet.as_view(DELETE),
        name='api_private_checklists_checklist_delete'
    ),
]