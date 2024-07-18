from django.shortcuts import render
from .models import *

from .forms import *

### FUNCIONES SIMPLES

def home(request):
    return render(request, "entidades/index.html")

def hosts(request):
     contexto = {"hosts": Hosts.objects.all()}
     return render(request, "entidades/hosts.html", contexto)

def vlans(request):
    contexto = {"vlans": Vlans.objects.all()}
    return render(request, "entidades/vlans.html", contexto)

def owners(request):
    contexto = {"owners": Owners.objects.all()}
    return render(request, "entidades/owners.html", contexto)

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

def vlansForm(request):
    if request.method == "POST":
        miForm = VlansForm(request.POST)
        if miForm.is_valid():
            vlan_name_form = miForm.cleaned_data.get("vlan_name")
            vlan_tag_form = miForm.cleaned_data.get("vlan_tag")
            vlan_desc_form = miForm.cleaned_data.get("vlan_desc")
            vlans = Vlans(vlan_name=vlan_name_form, vlan_tag=vlan_tag_form, vlan_desc=vlan_desc_form )
            vlans.save()
            contexto = {"vlans": Vlans.objects.all() }
            return render(request, "entidades/vlans.html", contexto)
    else:
        miForm = VlansForm()
    
    return render(request, "entidades/vlansForm.html", {"form": miForm})




#_______________________________________________________________
### OWNERS 

def ownersForm(request):
    if request.method == "POST":
        miForm = OwnersForm(request.POST)
        if miForm.is_valid():
            responsables_own_form = miForm.cleaned_data.get("responsables_own")
            proyecto_own_form = miForm.cleaned_data.get("proyecto_own")
            contacto_own_form = miForm.cleaned_data.get("contacto_own")
            owners = Owners(responsables_own=responsables_own_form, proyecto_own=proyecto_own_form, contacto_own=contacto_own_form )
            owners.save()
            contexto = {"owners": Owners.objects.all() }
            return render(request, "entidades/owners.html", contexto)
    else:
        miForm = OwnersForm()
    
    return render(request, "entidades/ownersForm.html", {"form": miForm})

#_______________________________________________________________
### CONTACTOS

def torresopsForm(request):
    if request.method == "POST":
        miForm = TorresOpsForm(request.POST)
        if miForm.is_valid():
            operadores_ops_form = miForm.cleaned_data.get("operadores_ops")
            team_ops_form = miForm.cleaned_data.get("team_ops")
            contacto_ops_form = miForm.cleaned_data.get("contacto_ops")
            torres = TorresOps(operadores_ops=operadores_ops_form, team_ops=team_ops_form, contacto_ops=contacto_ops_form )
            torres.save()
            contexto = {"torresops": TorresOps.objects.all() }
            return render(request, "entidades/torresops.html", contexto)
    else:
        miForm = TorresOpsForm()
    
    return render(request, "entidades/torresForm.html", {"form": miForm})
