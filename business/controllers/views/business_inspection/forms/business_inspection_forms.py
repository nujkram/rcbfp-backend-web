from django import forms

from business.models.business_inspection.business_inspection_model import BusinessInspection


class BusinessInspectionForm(forms.ModelForm):
    class Meta:
        model = BusinessInspection
        fields = '__all__'
