from django.db import models

# Create your models here.

class Sucursal(models.Model):
    direccion = models.CharField(max_length=50)
    horario = models.DateField()
    cantidad_empleados = models.IntegerField()


class Comida(models.Model):
    marca = models.CharField(max_length=50)
    kilogramos = models.IntegerField()
    tipo_comida = models.CharField(max_length=50)

class Clientes(models.Model):
    nombre = models.CharField(max_length=50) 
    apellido = models.CharField(max_length=50)    
    apellido = models.EmailField()   
    nombre_mascota = models.CharField(max_length=50)



class Direccion(models.Model):
    direccion = models.CharField(max_length=50)