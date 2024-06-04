from rest_framework import serializers
from .IntegralDataResponse import IntegralDataResponse

class IntegralDataSerializer(serializers.Serializer):
    x = serializers.ListField(child=serializers.FloatField())
    y = serializers.ListField(child=serializers.FloatField())
    yg = serializers.ListField(child=serializers.FloatField())
    total = serializers.FloatField()
    result = serializers.FloatField()
    def create(self, validated_data):
        return IntegralDataResponse(**validated_data)
