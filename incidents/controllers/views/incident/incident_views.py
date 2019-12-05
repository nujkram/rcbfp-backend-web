"""
rcbfp Module
---
incidents - Incident Master Model 0.0.1
This is the Master model for Incident

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
from incidents.models.incident.incident_models import Incident as Master

# Master Form
from incidents.controllers.views.incident.forms.incident_forms import IncidentForm as MasterForm


class IncidentListView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass


class IncidentCreateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class IncidentUpdateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class IncidentDeleteView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class IncidentDetailView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass
