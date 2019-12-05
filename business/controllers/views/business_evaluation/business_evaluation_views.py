"""
rcbfp Module
---
business - BusinessEvaluation Master Model 0.0.1
This is the Master model for BusinessEvaluation

---
Author: Mark Gersaniva
Email: mark.gersaniva@springvalley.tech
"""

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

# Master
from business.models.business_evaluation.business_evaluation_model import BusinessEvaluation as Master

# Master Form
from business.controllers.views.business_evaluation.forms.business_evaluation_forms import BusinessEvaluationForm as MasterForm


class BusinessEvaluationListView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass


class BusinessEvaluationCreateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessEvaluationUpdateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessEvaluationDeleteView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessEvaluationDetailView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass
