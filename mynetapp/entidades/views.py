from django.shortcuts import render

from django.urls import reverse_lazy
from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

### FUNCIONES SIMPLES

def home(request):
    return render(request, "entidades/index.html")

def hosts(request):
     contexto = {"hosts": Hosts.objects.all()}
     return render(request, "entidades/hosts.html", contexto)



def torresops(request):
    contexto = {"torresops": TorresOps.objects.all()}
    return render(request, "entidades/torresops.html", contexto)

def acerca(request):
    return render(request, "entidades/acerca.html")


###------------- FORMS & ACCIONES POR ENTIDAD -------------
### HOSTS

def hostsForm(request):
    if request.method == "POST":
        miForm = HostsForm(request.POST)
        if miForm.is_valid():
            host_name_host = miForm.cleaned_data.get("host_name")
            host_ip_host = miForm.cleaned_data.get("host_ip")
            host_vlan_host = miForm.cleaned_data.get("host_vlan")
            hosts = Hosts(host_name=host_name_host, host_ip=host_ip_host, host_vlan=host_vlan_host )
            hosts.save()
            contexto = {"hosts": Hosts.objects.all() }
            return render(request, "entidades/hosts.html", contexto)
    else:
        miForm = HostsForm()
    
    return render(request, "entidades/hostsForm.html", {"form": miForm})

def buscarHosts(request):
    return render(request, "entidades/buscarHosts.html")

def listarHosts(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        hosts = Hosts.objects.filter(host_name__icontains=patron)
        contexto = {'hosts': hosts}    
    else:
        contexto = {'hosts': Hosts.objects.all()}
        
    return render(request, "entidades/hosts.html", contexto)

def hostsUpdate(request, id_hosts):
    hosts = Hosts.objects.get(id=id_hosts)
    if request.method == "POST":
        miForm = HostsForm(request.POST)
        if miForm.is_valid():
            hosts.host_name = miForm.cleaned_data.get("host_name")
            hosts.host_ip = miForm.cleaned_data.get("host_ip")
            hosts.host_vlan = miForm.cleaned_data.get("host_vlan")
            hosts.save()
            contexto = {"hosts": Hosts.objects.all() }
            return render(request, "entidades/hosts.html", contexto)       
    else:
        miForm = HostsForm(initial={"host_name": hosts.host_name, "host_ip": hosts.host_ip, "host_vlan":hosts.host_vlan }) 
    
    return render(request, "entidades/hostsForm.html", {"form": miForm})

def hostsDelete(request, id_hosts):
    hosts = Hosts.objects.get(id=id_hosts)
    hosts.delete()
    contexto = {"hosts": Hosts.objects.all() }
    return render(request, "entidades/hosts.html", contexto)  

#_______________________________________________________________
### VLANS

class VlansList(ListView):
    model = Vlans

class VlansCreate(CreateView):
    model = Vlans
    fields = ["nombre", "vlan_TAG", "descripcion"]
    success_url = reverse_lazy("vlans")

class VlansUpdate(UpdateView):
    model = Vlans
    fields = ["nombre", "vlan_TAG", "descripcion"]
    success_url = reverse_lazy("vlans")

class VlansDelete(DeleteView):
    model = Vlans
    success_url = reverse_lazy("vlans")


#_______________________________________________________________
### OWNERS 

class OwnersList(ListView):
    model = Owners

class OwnersCreate(CreateView):
    model = Owners
    fields = ["responsables", "proyecto", "contacto"]
    success_url = reverse_lazy("owners")

class OwnersUpdate(UpdateView):
    model = Owners
    fields = ["responsables", "proyecto", "contacto"]
    success_url = reverse_lazy("owners")

class OwnersDelete(DeleteView):
    model = Owners
    success_url = reverse_lazy("owners")


#_______________________________________________________________
### CONTACTOS

class TorresOpsList(ListView):
    model = TorresOps

class TorresOpsCreate(CreateView):
    model = TorresOps
    fields = ["operadores", "team", "contacto"]
    success_url = reverse_lazy("torres")

class TorresOpsUpdate(UpdateView):
    model = TorresOps
    fields = ["operadores", "team", "contacto"]
    success_url = reverse_lazy("torres")

class TorresOpsDelete(DeleteView):
    model = TorresOps
    success_url = reverse_lazy("torres")


