from django.shortcuts import render
from .models import *

from .forms import *

# Create your views here.
def home(request):
    return render(request, "entidades/index.html")

def hosts(request):
     contexto = {"hosts": Hosts.objects.all()}
     return render(request, "entidades/hosts.html", contexto)

def vlans(request):
    contexto = {"vlans": Vlans.objects.all()}
    return render(request, "entidades/vlans.html", contexto)

def owners(request):
    contexto = {"vlans": Owners.objects.all()}
    return render(request, "entidades/owners.html", contexto)

def acerca(request):
    return render(request, "entidades/acerca.html")

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