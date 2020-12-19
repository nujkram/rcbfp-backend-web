from django import forms
from buildings.models.building.building_models import Building
from locations.models import Region, Province, City


class BuildingForm(forms.Form):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={'placeholder': 'Building Name', 'class': 'form-control'}))
    address = forms.CharField(required=True,
                              widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}))
    latitude = forms.CharField(required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Latitude', 'class': 'form-control'}))
    longitude = forms.CharField(required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Longitude', 'class': 'form-control'}))
    date_of_construction = forms.DateTimeField(required=True)
    floor_number = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Floor Number', 'class': 'form-control'}))
    height = forms.CharField(required=True,
                             widget=forms.NumberInput(attrs={'placeholder': 'Height', 'class': 'form-control'}))
    floor_area = forms.CharField(required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'Floor Area', 'class': 'form-control'}))
    total_floor_area = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Total Floor Area', 'class': 'form-control'}))
    beams = forms.CharField(required=True,
                            widget=forms.NumberInput(attrs={'placeholder': 'Beams', 'class': 'form-control'}))
    columns = forms.CharField(required=True,
                              widget=forms.NumberInput(attrs={'placeholder': 'Columns', 'class': 'form-control'}))
    flooring = forms.CharField(required=True,
                               widget=forms.NumberInput(attrs={'placeholder': 'Flooring', 'class': 'form-control'}))
    exterior_walls = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Exterior Walls', 'class': 'form-control'}))
    corridor_walls = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Corridor Walls', 'class': 'form-control'}))
    room_partitions = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Room Partitions', 'class': 'form-control'}))
    main_stair = forms.CharField(required=True,
                                 widget=forms.NumberInput(attrs={'placeholder': 'Main Stair', 'class': 'form-control'}))
    window = forms.CharField(required=True,
                             widget=forms.NumberInput(attrs={'placeholder': 'Window', 'class': 'form-control'}))
    ceiling = forms.CharField(required=True,
                              widget=forms.NumberInput(attrs={'placeholder': 'Ceiling', 'class': 'form-control'}))
    main_door = forms.CharField(required=True,
                                widget=forms.NumberInput(attrs={'placeholder': 'Main Door', 'class': 'form-control'}))
    trusses = forms.CharField(required=True,
                              widget=forms.NumberInput(attrs={'placeholder': 'Trusses', 'class': 'form-control'}))
    roof = forms.CharField(required=True,
                           widget=forms.NumberInput(attrs={'placeholder': 'Roof', 'class': 'form-control'}))
    entry_road_width = forms.CharField(required=True, widget=forms.NumberInput(
        attrs={'placeholder': 'Road Width', 'class': 'form-control'}))
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
