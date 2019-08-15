from django.contrib import admin
from .models.business.business_models import Business
from .models.business_application.business_application_model import BusinessApplication

class BusinessAdmin(admin.ModelAdmin):
  list_display = ('name', 'region', 'province', 'city', 'email', 'mobile_number')
  search_fields = ('name', 'owner_first_name', 'owner_last_name')
  list_filter = ('region', 'province', 'city')

class BusinessApplicationAdmin(admin.ModelAdmin):
  list_display = ('email', 'first_name', 'last_name')
  search_fields = ('email', 'first_name', 'last_name')

admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessApplication, BusinessApplicationAdmin)