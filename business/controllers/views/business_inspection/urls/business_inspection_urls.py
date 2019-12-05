from django.urls import path

from business.controllers.views.business_inspection import business_inspection_views as view

###############################################################################
# Views
###############################################################################

urlpatterns = [
    path(
        '<business>/business_inspection/list',
        view.BusinessInspectionListView.as_view(),
        name='business_inspection_list'
    ),
    path(
        '<business>/business_inspection/create',
        view.BusinessInspectionCreateView.as_view(),
        name='business_inspection_create'
    ),
    path(
        '<business>/business_inspection/<pk>/update',
        view.BusinessInspectionUpdateView.as_view(),
        name='business_inspection_update'
    ),
    path(
        '<business>/business_inspection/<pk>/detail',
        view.BusinessInspectionDetailView.as_view(),
        name='business_inspection_detail'
    ),
    path(
        '<business>/business_inspection/<pk>/delete',
        view.BusinessInspectionDeleteView.as_view(),
        name='business_inspection_delete'
    ),
]

