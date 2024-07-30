from django.db import models

# Create your models here.

# Modelo de negocio de la Aplicacion
class Hosts(models.Model):
    host_name = models.CharField(max_length=50)
    host_ip = models.CharField(max_length=18)
    host_vlan = models.IntegerField()

class Vlans(models.Model):
    nombre = models.CharField(max_length=60)
    vlan_TAG = models.IntegerField()
    descripcion = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.nombre}, {self.vlan_TAG}, {self.descripcion}" 

class Owners(models.Model):
    responsables = models.CharField(max_length=60)
    proyecto = models.CharField(max_length=60)
    contacto = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.responsables}, {self.proyecto}, {self.contacto}" 

class TorresOps(models.Model):
    operadores = models.CharField(max_length=60)
    team = models.CharField(max_length=60)
    contacto = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.operadores}, {self.team}, {self.contacto}" 

