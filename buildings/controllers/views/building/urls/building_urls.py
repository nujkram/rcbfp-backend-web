from django.urls import path

from buildings.controllers.views.building import building_views as view

###############################################################################
# Views
###############################################################################

urlpatterns = [
    path(
        '<buildings>/building/list',
        view.BuildingListView.as_view(),
        name='building_list'
    ),
    path(
        '<buildings>/building/create',
        view.BuildingCreateView.as_view(),
        name='building_create'
    ),
    path(
        '<buildings>/building/<pk>/update',
        view.BuildingUpdateView.as_view(),
        name='building_update'
    ),
    path(
        '<buildings>/building/<pk>/detail',
        view.BuildingDetailView.as_view(),
        name='building_detail'
    ),
    path(
        '<buildings>/building/<pk>/delete',
        view.BuildingDeleteView.as_view(),
        name='building_delete'
    ),
]

