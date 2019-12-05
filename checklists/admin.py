from django.contrib import admin

from checklists.models.checklist.checklist_models import Checklist


class ChecklistAdmin(admin.ModelAdmin):
    list_display = ('building', 'business', 'active', )
    search_fields = ('building', 'business',)
    list_filter = ('active',)


admin.site.register(Checklist, ChecklistAdmin)