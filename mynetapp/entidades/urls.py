
from django.urls import path, include
from entidades.views import *

urlpatterns = [
    path('', home, name="home"),
    path('hosts/', hosts, name="hosts"),
    path('vlans/', vlans, name="vlans"),

    path('owners/', owners, name="owners"),
    path('acerca/', acerca, name="acerca"),

    path('hostsForm/', hostsForm, name="hostsForm"),
    path('buscarHosts/', buscarHosts, name="buscarHosts"),
    path('listarHosts/', listarHosts, name="listarHosts"),
   
]
