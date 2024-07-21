from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm

## APLICAN SOBRE LAS CLASES
from django.contrib.auth.mixins import LoginRequiredMixin

## APLICAN SOBRE LAS FUNCIONES
from django.contrib.auth.decorators import login_required

### FUNCIONES SIMPLES

def home(request):
    return render(request, "entidades/index.html")

@login_required
def hosts(request):
     contexto = {"hosts": Hosts.objects.all()}
     return render(request, "entidades/hosts.html", contexto)

@login_required
def torresops(request):
    contexto = {"torresops": TorresOps.objects.all()}
    return render(request, "entidades/torresops.html", contexto)


def acerca(request):
    return render(request, "entidades/acerca.html")

###------------- FORMS & ACCIONES POR ENTIDAD -------------
### HOSTS

@login_required
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

@login_required
def buscarHosts(request):
    return render(request, "entidades/buscarHosts.html")

@login_required
def listarHosts(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        hosts = Hosts.objects.filter(host_name__icontains=patron)
        contexto = {'hosts': hosts}    
    else:
        contexto = {'hosts': Hosts.objects.all()}
        
    return render(request, "entidades/hosts.html", contexto)

@login_required
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

@login_required
def hostsDelete(request, id_hosts):
    hosts = Hosts.objects.get(id=id_hosts)
    hosts.delete()
    contexto = {"hosts": Hosts.objects.all() }
    return render(request, "entidades/hosts.html", contexto)  

#_______________________________________________________________
### VLANS

class VlansList(LoginRequiredMixin, ListView):
    model = Vlans

class VlansCreate(LoginRequiredMixin, CreateView):
    model = Vlans
    fields = ["nombre", "vlan_TAG", "descripcion"]
    success_url = reverse_lazy("vlans")

class VlansUpdate(LoginRequiredMixin, UpdateView):
    model = Vlans
    fields = ["nombre", "vlan_TAG", "descripcion"]
    success_url = reverse_lazy("vlans")

class VlansDelete(LoginRequiredMixin, DeleteView):
    model = Vlans
    success_url = reverse_lazy("vlans")


#_______________________________________________________________
### OWNERS 

class OwnersList(LoginRequiredMixin, ListView):
    model = Owners

class OwnersCreate(LoginRequiredMixin, CreateView):
    model = Owners
    fields = ["responsables", "proyecto", "contacto"]
    success_url = reverse_lazy("owners")

class OwnersUpdate(LoginRequiredMixin, UpdateView):
    model = Owners
    fields = ["responsables", "proyecto", "contacto"]
    success_url = reverse_lazy("owners")

class OwnersDelete(LoginRequiredMixin, DeleteView):
    model = Owners
    success_url = reverse_lazy("owners")


#_______________________________________________________________
### CONTACTOS

class TorresOpsList(LoginRequiredMixin, ListView):
    model = TorresOps

class TorresOpsCreate(LoginRequiredMixin, CreateView):
    model = TorresOps
    fields = ["operadores", "team", "contacto"]
    success_url = reverse_lazy("torres")

class TorresOpsUpdate(LoginRequiredMixin, UpdateView):
    model = TorresOps
    fields = ["operadores", "team", "contacto"]
    success_url = reverse_lazy("torres")

class TorresOpsDelete(LoginRequiredMixin, DeleteView):
    model = TorresOps
    success_url = reverse_lazy("torres")



# _________________________________________________________________ 
### LOGIN/OUT

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            return render(request, "entidades/index.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "entidades/login.html", {"form": miForm})

  
def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "entidades/registro.html", {"form": miForm}) 