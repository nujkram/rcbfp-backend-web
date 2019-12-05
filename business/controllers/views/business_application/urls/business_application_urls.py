from django.urls import path

from business.controllers.views.business_application import business_application_views as view

###############################################################################
# Views
###############################################################################

urlpatterns = [
    path(
        '<business>/business_application/list',
        view.BusinessApplicationListView.as_view(),
        name='business_application_list'
    ),
    path(
        '<business>/business_application/create',
        view.BusinessApplicationCreateView.as_view(),
        name='business_application_create'
    ),
    path(
        '<business>/business_application/<pk>/update',
        view.BusinessApplicationUpdateView.as_view(),
        name='business_application_update'
    ),
    path(
        '<business>/business_application/<pk>/detail',
        view.BusinessApplicationDetailView.as_view(),
        name='business_application_detail'
    ),
    path(
        '<business>/business_application/<pk>/delete',
        view.BusinessApplicationDeleteView.as_view(),
        name='business_application_delete'
    ),
]

