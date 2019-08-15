from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from accounts.constants import INSPECTOR, ADMIN, SUPERADMIN
from accounts.forms import RegisterForm, LoginForm
from accounts.models import Account
from helpers.errors import PrettyErrors


class AccountRegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegisterForm

        context = {
            'page_title': 'Registration',
            'local': 'register',
            'form': form,
        }

        return render(request, 'frontend/accounts/create.html', context)

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            account = Account.objects.create_user(
                email=email,
                password=password,
                user_type=INSPECTOR
            )

            user = authenticate(email=account.email, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Account created! Please fill in your profile info", extra_tags='success')
                return HttpResponseRedirect(reverse('backend_dashboard_home_view'))
            else:
                messages.error(request, "Unable to authenticate your account", extra_tags='danger')
                return HttpResponseRedirect(reverse('accounts_register_view'))
        else:
            errors = PrettyErrors(errors=form.errors)
            messages.error(request, errors.as_html(), extra_tags='danger')
            return HttpResponseRedirect(reverse('accounts_register_view'))


class AccountLoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm

        context = {
            'page_title': 'Login',
            'location': 'login',
            'form': form
        }

        return render(request, 'frontend/accounts/login.html', context)

    def post(self, request, *args, **kwargs):
        email = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = authenticate(email=email, password=password)

        if user is not None:
            if not user.is_active:
                messages.error(request, "User account is not active", extra_tags='danger')
                return HttpResponseRedirect(reverse('accounts_login_view'))

            login(request, user)
            user.regenerate_hash()
            messages.success(request, "Welcome to Safety Permit Decision Support System", extra_tags='success')

            if user.user_type == ADMIN:
                return HttpResponseRedirect(reverse('backend_dashboard_home_view'))
            elif user.user_type == INSPECTOR:
                return HttpResponseRedirect(reverse('backend_dashboard_home_view'))
            elif user.user_type == SUPERADMIN:
                return HttpResponseRedirect('/nOQD0no1oiuWSdp0SMwZ')
            else:
                return HttpResponseRedirect('/')
        else:
            messages.error(request, "You have entered an invalid credentials (email and/or password",
                           extra_tags='danger')
            return HttpResponseRedirect('/')


class AccountLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('frontend_home_view'))