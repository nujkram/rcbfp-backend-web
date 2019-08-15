from django.contrib import admin

from profiles.models import BaseProfile, ProfileMobtel, Gender


class BaseProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'rank')
    list_filter = ('gender', 'rank')
    search_fields = ('first_name', 'last_name', 'user', 'rank')

admin.site.register(BaseProfile, BaseProfileAdmin)


class ProfileMobtelAdmin(admin.ModelAdmin):
    list_display = ('number', 'carrier', 'is_public', 'is_active')
    list_filter = ('number', 'carrier', 'is_public', 'is_active')
    search_fields = ('number', 'carrier')

admin.site.register(ProfileMobtel, ProfileMobtelAdmin)


class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)

admin.site.register(Gender, GenderAdmin)