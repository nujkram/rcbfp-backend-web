from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic import DeleteView

from accounts.models import Account
from helpers.errors import PrettyErrors
from profiles.forms import ProfileMobtelForm
from profiles.models import ProfileMobtel


class ProfileMobtelCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        form = ProfileMobtelForm

        context = {
            'page_title': 'Add a Mobile Number',
            'mobtels': profile,
            'form': form
        }

        return render(request, 'backend/dashboard/mobtels/home.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        form = ProfileMobtelForm(request.POST)

        if form.is_valid():
            mobtel = form.save(commit=False)
            mobtel.profile = profile
            mobtel.save()

            messages.success(request, "Mobtel created", extra_tags='success')
            return HttpResponseRedirect(reverse('profiles_home_view'))
        else:
            errors = PrettyErrors(errors=form.errors)
            messages.error(request, errors.as_html(), extra_tags='danger')
            return HttpResponseRedirect(reverse('profiles_mobtel_create_view'))


class ProfileMobtelUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            mobtel = get_object_or_404(ProfileMobtel, pk=kwargs['pk'], profile=profile)
        except ProfileMobtel.DoesNotExist:
            mobtel = None
            HttpResponseRedirect(reverse('profiles_home_view'))

        form = ProfileMobtelForm(instance=mobtel)

        context = {
            'page_title': 'Update a Mobile Number',
            'mobtels': profile,
            'mobtel': mobtel,
            'form': form
        }

        return render(request, 'frontend/dashboard/mobtels/home.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            mobtel = get_object_or_404(ProfileMobtel, pk=kwargs['pk'], profile=profile)
        except ProfileMobtel.DoesNotExist:
            HttpResponseRedirect(reverse('profiles_home_view'))

        form = ProfileMobtelForm(request.POST, instance=mobtel)

        if form.is_valid():
            mobtel = form.save(commit=False)
            mobtel.profile = profile
            mobtel.save()

            messages.success(request, "Mobtel updated", extra_tags='success')
            return HttpResponseRedirect(reverse('profiles_home_view'))
        else:
            errors = PrettyErrors(errors=form.errors)
            messages.error(request, errors.as_html(), extra_tags='danger')
            return HttpResponseRedirect(reverse('profiles_mobtel_create_view'))


class ProfileMobtelDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            mobtel = get_object_or_404(ProfileMobtel, pk=kwargs['pk'], profile=profile)
        except ProfileMobtel.DoesNotExist:
            mobtel = None
            HttpResponseRedirect(reverse('profiles_home_view'))

        context = {
            'page_title': 'Delete a Mobile Number',
            'mobtel': mobtel,
            'mobtels': profile,
        }

        return render(request, 'frontend/dashboard/mobtels/delete.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            mobtel = get_object_or_404(ProfileMobtel, pk=kwargs['pk'], profile=profile)
        except ProfileMobtel.DoesNotExist:
            mobtel = None
            HttpResponseRedirect(reverse('profiles_home_view'))

        mobtel.delete()

        messages.success(request, "Mobtel deleted", extra_tags='success')
        return HttpResponseRedirect(reverse('profiles_home_view'))

