from django.db import models

# Create your models here.
class Vehicle(models.Model):
    marca = models.CharField("marca del carrro", max_length=45)
    sucursal = models.CharField("localidad de llegada", max_length=45)
    aspirante = models.CharField("aspirante al vehiculo", max_length=100)

    def __str__(self) -> str:
        return str(self.marca)