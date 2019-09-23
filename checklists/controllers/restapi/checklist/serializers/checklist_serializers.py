from rest_framework import serializers

# Master
from checklists.models.checklist_models import Checklist as Master


class ChecklistPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )


class ChecklistPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'
