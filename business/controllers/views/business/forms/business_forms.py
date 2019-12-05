from django import forms

from business.models.business.business_models import Business


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = '__all__'