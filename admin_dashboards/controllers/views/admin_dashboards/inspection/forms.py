from django import forms

from accounts.models import Account
from buildings.models.building.building_models import Building
from business.models import Business


class InspectionForm(forms.Form):
    inspection_date = forms.DateTimeField(required=True)

    user = forms.ModelChoiceField(
        queryset=Account.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    building = forms.ModelChoiceField(
        queryset=Building.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    business = forms.ModelChoiceField(
        queryset=Business.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )

