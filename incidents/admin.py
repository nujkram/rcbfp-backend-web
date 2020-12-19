from django.contrib import admin

from incidents.models.incident.incident_models import Incident, IncidentCoordinate


class IncidentAdmin(admin.ModelAdmin):
    list_display = ('business', 'building', 'incident_type', 'city')
    search_fields = ('business', 'building', 'region', 'province', 'city',)
    list_filter = ('city',)
    ordering = ('-created',)


admin.site.register(Incident, IncidentAdmin)


class IncidentCoordinateAdmin(admin.ModelAdmin):
    list_display = ('incident', 'lat', 'lng', 'created')
    search_fields = ('incident',)
    list_filter = ('incident',)
    ordering = ('-created',)


admin.site.register(IncidentCoordinate, IncidentCoordinateAdmin)
