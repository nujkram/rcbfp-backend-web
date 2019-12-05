"""
rcbfp Module
---
business - BusinessInspection Master Model 0.0.1
This is the Master model for BusinessInspection

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
from business.models.business_inspection.business_inspection_model import BusinessInspection as Master

# Master Form
from business.controllers.views.business_inspection.forms.business_inspection_forms import BusinessInspectionForm as MasterForm


class BusinessInspectionListView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass


class BusinessInspectionCreateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessInspectionUpdateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessInspectionDeleteView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessInspectionDetailView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass
