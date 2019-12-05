from django.urls import path

from business.controllers.views.business import business_views as view

###############################################################################
# Views
###############################################################################

urlpatterns = [
    path(
        '<business>/business/list',
        view.BusinessListView.as_view(),
        name='business_list'
    ),
    path(
        '<business>/business/create',
        view.BusinessCreateView.as_view(),
        name='business_create'
    ),
    path(
        '<business>/business/<pk>/update',
        view.BusinessUpdateView.as_view(),
        name='business_update'
    ),
    path(
        '<business>/business/<pk>/detail',
        view.BusinessDetailView.as_view(),
        name='business_detail'
    ),
    path(
        '<business>/business/<pk>/delete',
        view.BusinessDeleteView.as_view(),
        name='business_delete'
    ),
]

