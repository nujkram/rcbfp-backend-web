from django import forms

from profiles.models import Gender, BaseProfile, ProfileMobtel, ProfileAddress


class GenderForm(forms.ModelForm):
    class Meta:
        model = Gender
        fields = ('name',)


class BaseProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Format: YYYY-MM-DD (ex: 2018-10-15'

    class Meta:
        model = BaseProfile
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'date_of_birth',
            'marital_status',
            'rank'
        )


class BasicProfileForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = True

    class Meta:
        model = BaseProfile
        fields = (
            'first_name',
            'last_name'
        )
        required = fields


class ProfileCreateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = True
        self.fields['date_of_birth'].widget.attrs['placeholder'] = 'Format: YYYY-MM-DD (ex: 2018-10-15)'

    class Meta:
        model = BaseProfile
        fields = (
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'date_of_birth',
            'marital_status',
            'rank'
        )

        required = (
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'marital_status',
            'rank'
        )


class ProfileMobtelForm(forms.ModelForm):
    number = forms.CharField(help_text="Example: +63 910 1234567")

    class Meta:
        model = ProfileMobtel
        fields = (
            'number',
            'carrier',
        )


class ProfileAddressForm(forms.ModelForm):
    class Meta:
        model = ProfileAddress
        fields = (
            'address1',
            'address2',
            'zip_code',
            'city',
            'country'
        )


class ProfileUpdateForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.required:
            self.fields[field].required = True
        for field in self.Meta.disabled:
            self.fields[field].disabled = True

    class Meta:
        model = BaseProfile
        fields = (
            'first_name',
            'first_name',
            'middle_name',
            'last_name',
            'gender',
            'date_of_birth',
            'marital_status',
            'rank',
        )

        required = (
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
            'rank',
        )

        disabled = (
            'first_name',
            'last_name',
            'gender',
            'date_of_birth',
        )