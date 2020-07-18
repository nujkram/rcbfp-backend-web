from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View

from accounts.mixins.user_type_mixins import IsAdminViewMixin
from buildings.models.building.building_models import Building
from checklists.models.checklist.checklist_models import Checklist
from etl.loaders import checklist_regr
from incidents.models.incident.incident_models import Incident


class AdminDashboardAnalyticsLinearRegressionFormView(LoginRequiredMixin, IsAdminViewMixin, View):
    def get(self, request, *args, **kwargs):
        building_features = Building.analytics_features
        checklist_features = Checklist.analytics_features

        dependent_variables = ['count']
        dependent_variables += Incident.analytics_features

        context = {
            "page_title": f"Run Linear Regression",
            "menu_section": "analytics",
            "menu_subsection": "linear_regression",
            "menu_action": "create",
            "building_features": building_features,
            "checklist_features": checklist_features,
            "dependent_variables": dependent_variables
        }

        return render(request, "analytics/linear_regression/form.html", context)

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

        iv = request.POST['iv']

        result = checklist_regr(dvar=iv, building_features=building_features, checklist_features=checklist_features)

        context = {
            "page_title": f"Linear Regression Result",
            "menu_section": "analytics",
            "menu_subsection": "linear_regression",
            "menu_action": "detail",
            "summary": result['summary_html'],
            "test_Y": result['test_Y'],
            # "predicted_Y": result['predicted_Y']
        }
        return render(request, "analytics/linear_regression/detail.html", context)
