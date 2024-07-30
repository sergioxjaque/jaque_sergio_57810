
from django.urls import path, include
from entidades.views import *

from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('', home, name="home"),    
    path('acerca/', acerca, name="acerca"),

## HOSTS:
    path('hosts/', hosts, name="hosts"),
    path('hostsForm/', hostsForm, name="hostsForm"),
    path('buscarHosts/', buscarHosts, name="buscarHosts"),
    path('listarHosts/', listarHosts, name="listarHosts"),
    path('hostsUpdate/<id_hosts>', hostsUpdate, name="hostsUpdate"),
    path('hostsDelete/<id_hosts>', hostsDelete, name="hostsDelete"),
    

#________________________________________________________
## VLANS:
   
    #path('vlansForm/', vlansForm, name="vlansForm"),

    path('vlans/', VlansList.as_view(), name="vlans"),    
    path('vlansCreate/', VlansCreate.as_view(), name="vlansCreate"), 
    path('vlansUpdate/<int:pk>/', VlansUpdate.as_view(), name="vlansUpdate"), 
    path('vlansDelete/<int:pk>/', VlansDelete.as_view(), name="vlansDelete"),

#________________________________________________________
## OWNERS DE PROYECTOS O APPS:
  
    path('owners/', OwnersList.as_view(), name="owners"),    
    path('ownersCreate/', OwnersCreate.as_view(), name="ownersCreate"), 
    path('ownersUpdate/<int:pk>/', OwnersUpdate.as_view(), name="ownersUpdate"), 
    path('ownersDelete/<int:pk>/', OwnersDelete.as_view(), name="ownersDelete"),

#________________________________________________________
## CONTACTOS POR TORRES DE OPERACIONES:
    path('torresops/', TorresOpsList.as_view(), name="torresops"),    
    path('torresopsCreate/', TorresOpsCreate.as_view(), name="torresopsCreate"), 
    path('torresopsUpdate/<int:pk>/', TorresOpsUpdate.as_view(), name="torresopsUpdate"), 
    path('torresopsDelete/<int:pk>/', TorresOpsDelete.as_view(), name="torresopsDelete"),


# _________________________________________________________________ 
### LOGIN/OUT
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="entidades/logout.html"), name="logout"),
    path('registro/', register, name="registro"), 
]

