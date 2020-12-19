from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.tokens import default_token_generator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.views import PasswordContextMixin

from accounts.constants import USER_DASHBOARD_ROOTS
from accounts.controllers.views.forms.account_forms import LoginForm, AccountPasswordResetForm
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView
from django.views.decorators.csrf import csrf_protect


class AccountLoginView(View):
    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return HttpResponseRedirect(f'/{USER_DASHBOARD_ROOTS[request.user.user_type]}')

        form = LoginForm

        context = {
            "page_title": f"RCBFP: Login",
            "form": form,
            "location": "login"
        }

        return render(request, "accounts/login.html", context)

    def post(self, request, *args, **kwargs):

        form = LoginForm(data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                if not user.is_active:
                    messages.error(
                        request, "User account is not active", extra_tags="danger"
                    )
                else:
                    login(request, user)
                    messages.success(request, f"Welcome, {user}!", extra_tags="success")

                    next = request.GET.get('next', None)
                    if next:
                        return HttpResponseRedirect(next)
                    return HttpResponseRedirect(f'/{USER_DASHBOARD_ROOTS[user.user_type]}')
            else:
                messages.error(request, "Invalid credentials", extra_tags="danger")
        else:
            messages.error(request, form.errors, extra_tags="danger")

        context = {
            "page_title": f"Login",
            "form": form,
            "location": "login"
        }
        return render(request, "accounts/login.html", context)


class AccountLogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("accounts_login"))


class PasswordResetView(PasswordContextMixin, FormView):
    email_template_name = 'accounts/password_reset_email.html'
    extra_email_context = None
    form_class = AccountPasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = 'password_reset/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')
    template_name = 'accounts/password_reset_form.html'
    title = 'Password reset'
    token_generator = default_token_generator

    @method_decorator(csrf_protect)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': self.token_generator,
            'from_email': self.from_email,
            'email_template_name': self.email_template_name,
            'subject_template_name': self.subject_template_name,
            'request': self.request,
            'html_email_template_name': self.html_email_template_name,
            'extra_email_context': self.extra_email_context,
        }
        form.save(**opts)
        return super().form_valid(form)
