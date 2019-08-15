from django.urls import path

from profiles.modules.views import home as home_views
from profiles.modules.views import address as address_views
from profiles.modules.views import mobtels as mobtel_views

urlpatterns = [
    path('home', home_views.ProfileHomeView.as_view(), name='profiles_home_view'),
    path('create', home_views.ProfileCreateView.as_view(), name='profiles_create_view'),
    path('update', home_views.ProfileUpdateView.as_view(), name='profiles_update_view'),

    path('address/create', address_views.ProfileAddressCreateView.as_view(), name='profiles_address_create_view'),
    path('address/<pk>/update', address_views.ProfileAddressUpdateView.as_view, name='profiles_address_update_view'),
    path('address/<pk>/delete', address_views.ProfileAddressDeleteView.as_view(), name='profiles_address_delete_view'),

    path('mobtel/create', mobtel_views.ProfileMobtelCreateView.as_view(), name='profiles_mobtel_create_view'),
    path('mobtel/<pk>/update', mobtel_views.ProfileMobtelUpdateView.as_view(), name='profile_mobtel_update_view'),
    path('mobtel/<pk>/delete', mobtel_views.ProfileMobtelDeleteView.as_view(), name='profile_mobtel_delete_view'),

]