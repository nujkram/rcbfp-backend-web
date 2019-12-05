from rest_framework import serializers

# Master
from business.models.business_models import Business as Master


class BusinessPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )


class BusinessPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'
