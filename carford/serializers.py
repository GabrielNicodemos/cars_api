from rest_framework import serializers
from .models import Owner, Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarSalesSerializer(serializers.Serializer):
    model = serializers.CharField()
    count = serializers.IntegerField()

class OwnerSerializer(serializers.ModelSerializer):
    cars = CarSerializer(many=True, read_only=True)

    class Meta:
        model = Owner
        fields = '__all__'
