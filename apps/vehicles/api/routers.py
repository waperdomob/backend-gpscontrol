from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.vehicles.api.views import VehicleApiView, VehicleAPIViewDetail

router = DefaultRouter()


urlpatterns = [
    path('vehicles/', VehicleApiView.as_view(), name='vehicle-list'),
    path('vehicles/<int:pk>/', VehicleAPIViewDetail.as_view(), name='vehicle-detail'),
]
