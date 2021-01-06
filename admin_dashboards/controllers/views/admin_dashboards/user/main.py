from datetime import datetime

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template, render_to_string
from django.urls import reverse, reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.views import View
from django.core.paginator import Paginator
from django.contrib.auth.tokens import default_token_generator
from rest_framework.authtoken.models import Token

from accounts.constants import USER_TYPE_CHOICES, SUPERADMIN
from accounts.controllers.views.forms.account_forms import AccountPasswordResetForm
from accounts.mixins.user_type_mixins import IsAdminViewMixin

from accounts.models import Account as Master
from admin_dashboards.controllers.views.admin_dashboards.user.forms import UserForm as MasterForm
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils import six

"""
URLS
# User

from admin_dashboards.controllers.views.admin_dashboards.user import main as user_views

urlpatterns += {
    path(
        'user/list',
        user_views.AdminDashboardUserListView.as_view(),
        name='admin_dashboard_user_list'
    ),
    path(
        'user/<pk>/detail',
        user_views.AdminDashboardUserDetailView.as_view(),
        name='admin_dashboard_user_detail'
    ),
    path(
        'user/create',
        user_views.AdminDashboardUserCreateView.as_view(),
        name='admin_dashboard_user_create'
    ),
    path(
        'user/<pk>/update',
        user_views.AdminDashboardUserUpdateView.as_view(),
        name='admin_dashboard_user_update'
    ),
    path(
        'user/<pk>/delete',
        user_views.AdminDashboardUserDeleteView.as_view(),
        name='admin_dashboard_user_delete'
    )
}
"""


class AdminDashboardUserListView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    List view for Users.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - Optionally used more multi-user/multi-tenant apps to separate ownership
        - ex: company=kwargs.get('company')
    """

    def get(self, request, *args, **kwargs):
        obj_list = Master.objects.exclude(user_type=SUPERADMIN)
        paginator = Paginator(obj_list, 1000)
        page = request.GET.get('page')
        objs = paginator.get_page(page)

        context = {
            "page_title": f"Manage Users",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "list",
            "paginator": paginator,
            "objects": objs
        }

        return render(request, "user/list.html", context)


class AdminDashboardUserCreateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
        Create view for Users.

        Allowed HTTP verbs:
            - GET
            - POST

        Restrictions:
            - LoginRequired
            - Admin user

        Filters:
            - Optionally used more multi-user/multi-tenant apps to separate ownership
            - ex: company=kwargs.get('company')
        """

    def get(self, request, *args, **kwargs):
        form = MasterForm
        user_type = USER_TYPE_CHOICES

        context = {
            "page_title": "Create new User",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "create",
            "user_type": user_type,
            "form": form,
        }

        return render(request, "user/form.html", context)

    def post(self, request, *args, **kwargs):
        form = MasterForm(request.POST, request.FILES)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            user_type = form.cleaned_data['user_type']

            user = Master.objects.create(
                username=username,
                email=email,
                password=password1,
                user_type=user_type
            )

            if user:
                """ email """
                email_body = f"To initiate the password reset process for your {user.get_username} RCBFP Account," \
                             "click the link below:\n" \
                             "http://192.168.33.66:8000/account/forgot_password" \
                             "If clicking the link above doesn't work, please copy and paste the URL in a new browser" \
                             "window instead.\n\n" \
                             "Sincerely,\n" \
                             "The RCBFP Team"
                message = render_to_string('accounts/password_reset_email.html', {
                    'user': user,
                    'protocol': 'http',
                    'domain': 'http://192.168.33.66:8000',
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user)
                })

                email_subject = 'Welcome to RCBFP!'
                from_email = 'mark.gersaniva@pueblodepanay.com'
                to_email = email
                mail = EmailMultiAlternatives(
                    subject=email_subject,
                    body=email_body,
                    from_email=from_email,
                    to=[to_email],
                )

                try:
                    mail.attach_alternative(message, "text/html")
                except TemplateDoesNotExist:
                    pass

                mail.send()
                """ /email """

                messages.success(request, 'User created!', extra_tags='success')
                return HttpResponseRedirect(reverse('admin_dashboard_user_detail', kwargs={'pk': user.pk}))
            else:
                messages.error(request, form.errors, extra_tags='danger')
                return HttpResponseRedirect(reverse('admin_dashboard_user_create'))
        else:
            messages.error(request, form.errors, extra_tags='danger')
            return HttpResponseRedirect(reverse('admin_dashboard_user_create'))


class AdminDashboardUserDetailView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Create view for Users.

    Allowed HTTP verbs:
        - GET

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))

        context = {
            "page_title": f"User: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "detail",
            "obj": obj,
        }

        return render(request, "user/detail.html", context)


class AdminDashboardUserUpdateView(LoginRequiredMixin, IsAdminViewMixin, View):
    """
    Update view for User.

    Allowed HTTP verbs:
        - GET
        - POST

    Restrictions:
        - LoginRequired
        - Admin user

    Filters:
        - pk = kwargs.get('pk')
    """

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        form = MasterForm(instance=obj)
        context = {
            "page_title": f"Update User: {obj}",
            "menu_section": "admin_dashboards",
            "menu_subsection": "admin_dashboards",
            "menu_action": "update",
            "obj": obj,
            "form": form,
        }

        return render(request, "user/form.html", context)

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(Master, pk=kwargs.get('pk', None))
        form = MasterForm(request.POST, instance=obj)

        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user_type = form.cleaned_data['user_type']
            is_active = form.cleaned_data['is_active']

            user = Master.objects.get(pk=obj.pk)

            user.set_password(password)
            user.email = email
            user.user_type = user_type
            user.is_active = is_active

            user.save()

            messages.success(
                request,
                f'{obj} updated!',
                extra_tags='success'
            )

            return HttpResponseRedirect(
                reverse(
                    'admin_dashboard_user_detail',
                    kwargs={
                        'pk': obj.pk
                    }
                )
            )
        else:
            context = {
                "page_title": f"Update User: {obj}",
                "menu_section": "admin_dashboards",
                "menu_subsection": "admin_dashboards",
                "menu_action": "update",
                "obj": obj,
                "form": form
            }

            messages.error(
                request,
                'There were errors processing your request:',
                extra_tags='danger'
            )
            return render(request, "user/form.html", context)


class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        login_timestamp = '' if user.last_login is None else user.last_login.replace(microsecond=0, tzinfo=None)
        return (
                six.text_type(user.pk) + user.password + six.text_type(login_timestamp) + six.text_type(timestamp)
        )


class PasswordResetToken(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
                six.text_type(user.pk) + six.text_type(timestamp)
        )


account_activation_token = AccountActivationTokenGenerator()
password_reset_token = PasswordResetToken()
