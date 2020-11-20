from django.urls import path
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView

from accounts.controllers.views.account_views import AccountLoginView, AccountLogoutView

urlpatterns = [
    path('login', AccountLoginView.as_view(), name='accounts_login'),
    path('logout', AccountLogoutView.as_view(), name='accounts_logout'),
    path('password/reset/', PasswordResetView.as_view(),
         {'post_reset_redirect': '/account/password/reset/done/'},
         name="password_reset"),
    path('password/reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),
         {'post_reset_redirect': '/account/password/complete/'},
         name='password_reset_confirm'
         ),
    path('password/reset/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
