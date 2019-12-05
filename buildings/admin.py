from django.contrib import admin

from buildings.models.building.building_models import Building


class BuildingAdmin(admin.ModelAdmin):
  list_display = ('name', 'address', 'region', 'province', 'city')
  search_fields = ('name',)
  list_filter = ('region',)

admin.site.register(Building, BuildingAdmin)