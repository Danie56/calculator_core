from rest_framework import serializers

from .integral_manage import solve_integrals
from .models import Integral
class IntegralSerializer(serializers.ModelSerializer):
    class Meta:
        model = Integral
        fields = ('id','type_method','expression','sub_intervals','result')
        read_only_fields=('result', )
    def create(self, validated_data):
        expression= validated_data['expression']
        sub_intervals=validated_data['sub_intervals']
        type_method=validated_data['type_method']
        result_object = solve_integrals(expression, sub_intervals, type_method)
    
        validated_data['result']= result_object.result
        Integral.objects.create(**validated_data) 

        return result_object
