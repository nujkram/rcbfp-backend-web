from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View

from accounts.models import Account
from helpers.errors import PrettyErrors
from profiles.forms import ProfileAddressForm
from profiles.models import ProfileAddress


class ProfileAddressCreateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        form = ProfileAddressForm

        context = {
            'page_title': 'Add an address',
            'mobtels': profile,
            'form': form
        }

        return render(request, 'frontend/dashboard/addresses/home.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        form = ProfileAddressForm(request.POST)

        if form.is_valid():
            address = form.save(commit=False)
            address.profile = profile
            address.save()

            messages.success(request, "Address created", extra_tags='success')
            return HttpResponseRedirect(reverse('profiles_home_view'))
        else:
            errors = PrettyErrors(errors=form.errors)
            messages.error(request, errors.as_html(), extra_tags='danger')
            return HttpResponseRedirect(reverse('profiles_address_create_view'))


class ProfileAddressUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            address = get_object_or_404(ProfileAddress, pk=kwargs['pk'], profile=profile)
        except ProfileAddress.DoesNotExist:
            address = None
            HttpResponseRedirect(reverse('profiles_home_view'))

        form = ProfileAddressForm(instance=address)

        context = {
            'page_title': 'Update an address',
            'mobtels': profile,
            'address': address,
            'form': form
        }

        return render(request, 'frontend/dashboard/addresses/home.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            address = get_object_or_404(ProfileAddress, pk=kwargs['pk'], profile=profile)
        except ProfileAddress.DoesNotExist:
            HttpResponseRedirect(reverse('profiles_home_view'))

        form = ProfileAddressForm(request.POST, instance=address)

        if form.is_valid():
            address = form.save(commit=False)
            address.profile = profile
            address.save()

            messages.success(request, "Address updated", extra_tags='success')
            return HttpResponseRedirect(reverse('profiles_home_view'))
        else:
            errors = PrettyErrors(errors=form.errors)
            messages.error(request, errors.as_html(), extra_tags='danger')
            return HttpResponseRedirect(reverse('profiles_address_create_view'))


class ProfileAddressDeleteView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            address = get_object_or_404(ProfileAddress, pk=kwargs['pk'], profile=profile)
        except ProfileAddress.DoesNotExist:
            address = None
            HttpResponseRedirect(reverse('profiles_home_view'))

        context = {
            'page_title': 'Delete an address',
            'address': address,
            'mobtels': profile,
        }

        return render(request, 'frontend/dashboard/addresses/delete.html', context)

    def post(self, request, *args, **kwargs):
        user = Account.objects.get(pk=request.user.pk)
        profile = user.base_profile()

        if not profile.is_active:
            return HttpResponseRedirect(reverse('profiles_create_view'))

        try:
            address = get_object_or_404(ProfileAddress, pk=kwargs['pk'], profile=profile)
        except ProfileAddress.DoesNotExist:
            address = None
            HttpResponseRedirect(reverse('profiles_home_view'))

        address.delete()

        messages.success(request, "Address deleted", extra_tags='success')
        return HttpResponseRedirect(reverse('profiles_home_view'))

