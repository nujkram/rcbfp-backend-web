from django.contrib import admin

from checklists.models.checklist.checklist_models import Checklist


class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('building', 'business', 'status', 'active',)
    search_fields = ('building__name', 'business__name')
    list_filter = ('active',)
    ordering = ('building__name',)


admin.site.register(Checklist, ChecklistAdmin)
