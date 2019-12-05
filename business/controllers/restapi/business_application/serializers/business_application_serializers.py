from rest_framework import serializers

# Master
from business.models.business_application_models import BusinessApplication as Master


class BusinessApplicationPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )


class BusinessApplicationPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'
