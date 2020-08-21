from django.contrib import admin

from business.models import BusinessEvaluation, BusinessInspection
from .models.business.business_models import Business
from .models.business_application.business_application_model import BusinessApplication


# Register your models here.
class BusinessAdmin(admin.ModelAdmin):
    list_display = ('name', 'building', 'region', 'province', 'city', 'email', 'mobile_number')
    search_fields = ('name', 'owner_first_name', 'owner_last_name')
    list_filter = ('active', )
    ordering = ('-created',)


class BusinessApplicationAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('-created',)

class BusinessEvaluationAdmin(admin.ModelAdmin):
    list_display = ('business', 'approved')
    search_fields = ('business',)
    list_filter = ('approved',)
    ordering = ('-created',)

class BusinessInspectionAdmin(admin.ModelAdmin):
    list_display = ('business', 'approved')
    search_fields = ('business',)
    list_filter = ('approved',)
    ordering = ('-created',)

admin.site.register(Business, BusinessAdmin)
admin.site.register(BusinessApplication, BusinessApplicationAdmin)
admin.site.register(BusinessEvaluation, BusinessEvaluationAdmin)
admin.site.register(BusinessInspection, BusinessInspectionAdmin)
