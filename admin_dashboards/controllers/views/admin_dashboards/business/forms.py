from django import forms

from buildings.models.building.building_models import Building
from locations.models import Region, Province, City


class BusinessForm(forms.Form):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nature = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    owner_first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    owner_middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    owner_last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    landline = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    mobile_number = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    building = forms.ModelChoiceField(
        queryset=Building.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    region = forms.ModelChoiceField(
        queryset=Region.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    province = forms.ModelChoiceField(
        queryset=Province.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    city = forms.ModelChoiceField(
        queryset=City.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
