"""
rcbfp Module
---
checklists - Checklist Master Model 0.0.1
This is the Master model for Checklist

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
from checklists.models.checklist.checklist_models import Checklist as Master

# Master Form
from checklists.controllers.checklist.forms.checklist_forms import ChecklistForm as MasterForm


class ChecklistListView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass


class ChecklistCreateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class ChecklistUpdateView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class ChecklistDeleteView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass

    def post(self, request, *args, **kwargs):
        pass


class ChecklistDetailView(
    LoginRequiredMixin,
    View
):
    def get(self, request, *args, **kwargs):
        pass
