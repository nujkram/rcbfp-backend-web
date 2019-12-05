from rest_framework import serializers

# Master
from business.models.business_evaluation_models import BusinessEvaluation as Master


class BusinessEvaluationPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = (
            'id',
        )


class BusinessEvaluationPrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'
