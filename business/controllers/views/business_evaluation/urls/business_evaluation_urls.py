from django.urls import path

from business.controllers.views.business_evaluation import business_evaluation_views as view

###############################################################################
# Views
###############################################################################

urlpatterns = [
    path(
        '<business>/business_evaluation/list',
        view.BusinessEvaluationListView.as_view(),
        name='business_evaluation_list'
    ),
    path(
        '<business>/business_evaluation/create',
        view.BusinessEvaluationCreateView.as_view(),
        name='business_evaluation_create'
    ),
    path(
        '<business>/business_evaluation/<pk>/update',
        view.BusinessEvaluationUpdateView.as_view(),
        name='business_evaluation_update'
    ),
    path(
        '<business>/business_evaluation/<pk>/detail',
        view.BusinessEvaluationDetailView.as_view(),
        name='business_evaluation_detail'
    ),
    path(
        '<business>/business_evaluation/<pk>/delete',
        view.BusinessEvaluationDeleteView.as_view(),
        name='business_evaluation_delete'
    ),
]

