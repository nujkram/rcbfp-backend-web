from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from buildings.models.building.building_models import Building
from checklists.models.checklist.checklist_models import Checklist
from etl.loaders import checklist_dtree
from incidents.models.incident.incident_models import Incident


class AdminDashboardAnalyticsDecisionTreeFormView(LoginRequiredMixin, IsAdminViewMixin, View):
    def get(self, request, *args, **kwargs):
        building_features = Building.analytics_features
        checklist_features = Checklist.analytics_features

        dependent_variables = ['has_incident']
        d_tree = f'{settings.MEDIA_URL}models/trees/checklist_dtree--1600174486.927769.png'
        context = {
            "page_title": f"Run Decision Tree",
            "menu_section": "analytics",
            "menu_subsection": "decision_tree",
            "menu_action": "create",
            "building_features": building_features,
            "checklist_features": checklist_features,
            "dependent_variables": dependent_variables,
            "image": d_tree
        }

        return render(request, "analytics/decision_tree/form.html", context)

    def post(self, request, *args, **kwargs):
        __building_features = request.POST['building_features'].split(" ")
        __checklist_features = request.POST['checklist_features'].split(" ")

        building_features = []
        checklist_features = []

        for bf in __building_features:
            bf = bf.strip()
            if bf:
                building_features.append(bf)

        for cf in __checklist_features:
            cf = cf.strip()
            if cf:
                checklist_features.append(cf)

        checklists = Checklist.objects.all()
        iv = request.POST['iv']

        result = checklist_dtree(dvar=iv, building_features=building_features, checklist_features=checklist_features, checklists=checklists)

        context = {
            "page_title": f"Decision Tree Result",
            "menu_section": "analytics",
            "menu_subsection": "decision_tree",
            "menu_action": "detail",
            "image": result['image'],
            "text": result['text']
        }
        return render(request, "analytics/decision_tree/detail.html", context)
