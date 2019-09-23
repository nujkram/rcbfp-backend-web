from rest_framework import serializers

# Master
from buildings.models.building_models import Building as Master


class BuildingPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )


class BuildingPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'
