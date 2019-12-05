"""
rcbfp Module
---
business - BusinessApplication Master Model 0.0.1
This is the Master model for BusinessApplication

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
from business.models.business_application.business_application_model import BusinessApplication as Master

# Master Form
from business.controllers.views.business_application.forms.business_application_forms import \
    BusinessApplicationForm as MasterForm


class BusinessApplicationListView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass


class BusinessApplicationCreateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessApplicationUpdateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessApplicationDeleteView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class BusinessApplicationDetailView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass
