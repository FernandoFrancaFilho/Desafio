from rest_framework import serializers
from car.models import Carro, Cnh

class CarroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carro
        fields = '__all__'

class CnhSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cnh
        fields = '__all__'