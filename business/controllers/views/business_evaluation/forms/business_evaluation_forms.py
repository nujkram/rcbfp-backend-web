from django import forms

from business.models.business_evaluation.business_evaluation_model import BusinessEvaluation


class BusinessEvaluationForm(forms.ModelForm):
    class Meta:
        model = BusinessEvaluation
        fields = '__all__'
