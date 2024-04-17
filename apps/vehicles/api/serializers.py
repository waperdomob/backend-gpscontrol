from rest_framework import serializers
from apps.vehicles.models import Vehicle

#serializer para listar, crear y detallar Vehicles
class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'