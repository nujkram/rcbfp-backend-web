from django import forms

from buildings.models.building.building_models import Building
from business.models import Business
from incidents.constants import INCIDENT_TYPE_CHOICES
from incidents.models import Incident
from locations.models import Region, Province, City


class IncidentForm(forms.Form):
    first_name = forms.CharField(required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    middle_name = forms.CharField(required=True,
                                  widget=forms.TextInput(attrs={'placeholder': 'Middle Name', 'class': 'form-control'}))
    phone = forms.CharField(required=True,
                            widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    address = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    image = forms.ImageField(required=False)
    incident_type = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Incident Type', 'class': 'form-control'}))
    property_damage = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Property Damage', 'class': 'form-control'}))
    casualties = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Casualties', 'class': 'form-control'}))
    major_injuries = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Major Injuries', 'class': 'form-control'}))
    minor_injuries = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Minor Injuries', 'class': 'form-control'}))
    intensity = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Intensity', 'class': 'form-control'}))
    severity = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Severity', 'class': 'form-control'}))
    duration = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'type': 'number', 'placeholder': 'Duration', 'class': 'form-control'}))
    building = forms.ModelChoiceField(
        queryset=Building.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    business = forms.ModelChoiceField(
        queryset=Business.objects.all(),
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
    latitude = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Latitude', 'class': 'form-control'}))
    longitude = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Longitude', 'class': 'form-control'}))
