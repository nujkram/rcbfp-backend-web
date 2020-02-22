from django import forms
from business.models.business_application.business_application_model import BusinessApplication


class BusinessApplicationForm(forms.ModelForm):
    class Meta:
        model = BusinessApplication
        fields = '__all__'