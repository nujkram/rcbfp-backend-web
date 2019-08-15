from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path

from accounts.modules.views import auth as auth_views

urlpatterns = [
    path('register', auth_views.AccountRegistrationView.as_view(), name='accounts_register_view'),
    path('login', auth_views.AccountLoginView.as_view(), name='accounts_login_view'),
    path('logout', auth_views.AccountLogoutView.as_view(), name='accounts_logout_view'),
    path('password/reset', PasswordResetView.as_view(),
         {'post_reset_redirect': '/account/password/reset/done/'}, name='password_reset'),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         {'post_reset_redirect': '/account/password/complete/'},
         name='password_reset_confirm'
         ),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]