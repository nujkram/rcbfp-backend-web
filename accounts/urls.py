from django.urls import path
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth import views as auth_views

from accounts.controllers.views.account_views import AccountLoginView, AccountLogoutView
from accounts.controllers.views.account_views import PasswordResetView as ResetPass

urlpatterns = [
    path('login', AccountLoginView.as_view(), name='accounts_login'),
    path('logout', AccountLogoutView.as_view(), name='accounts_logout'),
    path('forgot_password', PasswordResetView.as_view(), name='forgot_password'),
    path('reset_password', ResetPass.as_view(), name='reset_password'),
    path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/(<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
