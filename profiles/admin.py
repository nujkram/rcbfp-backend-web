from django.contrib import admin

# Register your models here.
from profiles.models import Profile
from profiles.models.profile_models import Gender


class ProfileAdmin(admin.ModelAdmin):
  list_display = ('account', 'first_name', 'last_name',)
  search_fields = ('first_name', 'middle_name', 'last_name',)


class GenderAdmin(admin.ModelAdmin):
  list_display = ('name',)
  search_fields = ('name',)

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Gender, GenderAdmin)
