from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

from apps.vehicles.models import Vehicle
from apps.vehicles.api.serializers import VehicleSerializer

class VehicleApiView(APIView):
    """Conjunto de vistas para el modelo Vehicle."""

    def get(self, request):
        queryset = Vehicle.objects.all().order_by("id")
        serializer = VehicleSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = VehicleSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
class VehicleAPIViewDetail(APIView):
    def get_object(self, pk):
        try:
            return Vehicle.objects.get(pk=pk)
        except Vehicle.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serializer = VehicleSerializer(data)  
        return Response(serializer.data)

    def put(self, request, **kwargs):
        pk = kwargs.get('pk')
        vehicle = Vehicle.objects.get(pk=pk)
        serializer = VehicleSerializer(vehicle, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        vehicle = Vehicle.objects.get(pk=pk)
        vehicle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)