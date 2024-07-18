
from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),    
    path('acerca/', acerca, name="acerca"),

## HOSTS:
    path('hosts/', hosts, name="hosts"),
    path('hostsForm/', hostsForm, name="hostsForm"),
    path('buscarHosts/', buscarHosts, name="buscarHosts"),
    path('listarHosts/', listarHosts, name="listarHosts"),
    path('hostsUpdate/<id_hosts>', hostsUpdate, name="hostsUpdate"),

#________________________________________________________
## VLANS:
    path('vlans/', vlans, name="vlans"),
    path('vlansForm/', vlansForm, name="vlansForm"),

#________________________________________________________
## OWNERS:
    path('owners/', owners, name="owners"),
    path('ownersForm/', ownersForm, name="ownersForm"),

#________________________________________________________
## CONTACTOS:

    path('torresops/', torresops, name="torresops"),
    path('torresForm/', torresopsForm, name="torresForm"),
#________________________________________________________
]
