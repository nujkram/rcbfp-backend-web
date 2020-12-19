from django.contrib import admin

from inspections.models.inspection_schedule.models import InspectionSchedule


class InspectionScheduleAdmin(admin.ModelAdmin):
    list_display = ['id', 'created']
    list_filter = ['id']
    search_fields = ['id']
    ordering = ['-created']


admin.site.register(InspectionSchedule, InspectionScheduleAdmin)
