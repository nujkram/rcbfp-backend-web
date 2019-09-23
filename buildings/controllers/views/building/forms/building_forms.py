from django import forms

from buildings.models.building_models import Building


class BuildingForm(forms.ModelForm):
    class Meta:
        model = Building
        fields = '__all__'