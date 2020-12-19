from django import forms

from buildings.models.building.building_models import Building
from business.models import Business


class ChecklistForm(forms.Form):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    middle_name = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    policy_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    building_permit = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    occupancy_permit = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fsic_control_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fsic_fee = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_drill_certificate = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    violation_control_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    electrical_inspection_no = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    sectional_occupancy = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    exits_count = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exits_width = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    exits_accessible = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    termination_of_exit = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exits_enclosure_provided = forms.BooleanField(required=False,
                                                  widget=forms.TextInput(attrs={'class': 'form-control'}))
    exits_enclosure_construction = forms.CharField(required=False,
                                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    exits_fire_doors_provided = forms.BooleanField(required=False,
                                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    exits_fire_door_construction = forms.CharField(required=False,
                                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    stairs_count = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    stairs_enclosure_provided = forms.BooleanField(required=False,
                                                   widget=forms.TextInput(attrs={'class': 'form-control'}))
    stairs_enclosure_construction = forms.CharField(required=False,
                                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    stairs_fire_doors_provided = forms.BooleanField(required=False,
                                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    stairs_fire_door_construction = forms.CharField(required=False,
                                                    widget=forms.TextInput(attrs={'class': 'form-control'}))
    other_details = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))

    emergency_light = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    exit_signs_illuminated = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_extinguisher_count = forms.IntegerField(required=False,
                                                 widget=forms.NumberInput(attrs={'class': 'form-control'}))
    fire_extinguisher_accessible = forms.BooleanField(required=False,
                                                      widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_extinguisher_conspicuous_location = forms.BooleanField(required=False,
                                                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    fire_alarm = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    detectors = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    control_panel_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    control_panel_functional = forms.BooleanField(required=False,
                                                  widget=forms.TextInput(attrs={'class': 'form-control'}))

    hazardous_materials = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    hazardous_materials_properly_stored = forms.BooleanField(required=False,
                                                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    no_smoking_sign = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    smoking_permitted = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    smoking_area_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    storage_location = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    safety_device_for_lpg = forms.BooleanField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    oven_used = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    kind_of_fuel = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    smoke_hood = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    spark_arrester = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    partition_construction = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    defects = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    building = forms.ModelChoiceField(queryset=Building.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    business = forms.ModelChoiceField(queryset=Business.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
    building_permit_date_issued = forms.DateTimeField(required=False)
    occupancy_permit_date_issued = forms.DateTimeField(required=False)
    fsic_date_issued = forms.DateTimeField(required=False)
    fire_drill_certificate_date_issued = forms.DateTimeField(required=False)
    violation_control_no_date_issued = forms.DateTimeField(required=False)
    electrical_inspection_date_issued = forms.DateTimeField(required=False)
    insurance_date_issued = forms.DateTimeField(required=False)
    date_checked = forms.DateTimeField(required=False)
    notes = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    recommendations = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))