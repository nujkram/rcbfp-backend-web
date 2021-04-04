from django.contrib import admin

from .models.business.business_models import Business


# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'region', 'province', 'city', 'email', 'mobile_number')
    search_fields = ('name', 'owner_first_name', 'owner_last_name')
    list_filter = ('active',)
    ordering = ('building__name',)


admin.site.register(Business, BusinessAdmin)
