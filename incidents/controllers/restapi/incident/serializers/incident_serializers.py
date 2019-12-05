from rest_framework import serializers

# Master
from incidents.models.incident_models import Incident as Master


class IncidentPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )


class IncidentPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'
