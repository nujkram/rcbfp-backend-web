from django.urls import path

from checklists.controllers.views.checklist import checklist_views as view

###############################################################################
# Views
###############################################################################

urlpatterns = [
    path(
        '<checklists>/checklist/list',
        view.ChecklistListView.as_view(),
        name='checklist_list'
    ),
    path(
        '<checklists>/checklist/create',
        view.ChecklistCreateView.as_view(),
        name='checklist_create'
    ),
    path(
        '<checklists>/checklist/<pk>/update',
        view.ChecklistUpdateView.as_view(),
        name='checklist_update'
    ),
    path(
        '<checklists>/checklist/<pk>/detail',
        view.ChecklistDetailView.as_view(),
        name='checklist_detail'
    ),
    path(
        '<checklists>/checklist/<pk>/delete',
        view.ChecklistDeleteView.as_view(),
        name='checklist_delete'
    ),
]

