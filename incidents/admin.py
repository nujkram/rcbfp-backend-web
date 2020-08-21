from django.contrib import admin

from incidents.models.incident.incident_models import Incident


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('business', 'building', 'incident_type', 'city')
    search_fields = ('business', 'building', 'region', 'province', 'city',)
    list_filter = ('city',)
    ordering = ('-created',)


admin.site.register(Incident, IncidentAdmin)
