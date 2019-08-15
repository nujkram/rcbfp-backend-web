from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from accounts.models import Account
from helpers.errors import PrettyErrors
from profiles.forms import ProfileCreateForm, ProfileAddressForm, ProfileUpdateForm


class ProfileHomeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profile_create_view'))

        context = {
            'page_title': 'Profile',
            'mobtels': profile
        }

        return render(request, 'backend/dashboard/profile/create.html', context)


class ProfileCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()
        form = ProfileCreateForm(instance=profile)

        context = {
            'page_title': 'Profile',
            'location': 'create',
            'profile': profile,
            'form': form
        }

        return render(request, 'backend/dashboard/profile/create.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()
        form = ProfileCreateForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_active = True
            profile.save()

            messages.success(request, "Profile updated", extra_tags='success')
            return HttpResponseRedirect(reverse('backend_dashboard_home_view'))
        else:
            errors = PrettyErrors(errors=form.errors)
            messages.error(request, errors.as_html(), extra_tags='danger')
            # return HttpResponseRedirect(reverse('profiles_create_view'))
            return HttpResponseRedirect(reverse('profiles_create_view'))


class ProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()
        form = ProfileUpdateForm(instance=profile)

        context = {
            'page_title': 'Profile',
            'location': 'update',
            'profile': profile,
            'form': form
        }

        return render(request, 'backend/dashboard/profile/create.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()
        form = ProfileUpdateForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.is_active = True
            profile.save()

            messages.success(request, "Profile updated", extra_tags='success')
            return HttpResponseRedirect(reverse('profiles_create_view'))
        else:
            errors = PrettyErrors(errors=form.errors)
            messages.error(request, errors.as_html(), extra_tags="danger")
            return HttpResponseRedirect(reverse('profiles_create_view'))