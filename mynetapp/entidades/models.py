from django.db import models

# Create your models here.

# Modelo de negocio de la Aplicacion
class Hosts(models.Model):
    host_name = models.CharField(max_length=50)
    host_ip = models.CharField(max_length=18)
    host_vlan = models.IntegerField()

class Vlans(models.Model):
    vlan_nombre = models.CharField(max_length=60)
    vlan_tag = models.IntegerField()
    vlan_desc = models.CharField(max_length=60)

class Owners(models.Model):
    resposables = models.CharField(max_length=60)
    proyecto = models.CharField(max_length=60)
    contacto = models.CharField(max_length=60)

