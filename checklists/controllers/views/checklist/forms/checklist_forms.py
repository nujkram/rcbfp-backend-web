from django import forms

from checklists.models.checklist_models import Checklist


class ChecklistForm(forms.ModelForm):
    class Meta:
        model = Checklist
        fields = '__all__'