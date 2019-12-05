from rest_framework import serializers

# Master
from business.models.business_inspection_models import BusinessInspection as Master


class BusinessInspectionPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )


class BusinessInspectionPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'
