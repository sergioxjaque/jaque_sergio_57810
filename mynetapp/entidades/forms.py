from django import forms 

class HostsForm(forms.Form):
    host_name = forms.CharField(max_length=50, required=True, label="Hostname")
    host_ip = forms.CharField(required=True, label="Direccion IP")
    host_vlan = forms.IntegerField(required=True, label="VLAN TAG")


class VlansForm(forms.Form):
    vlan_name = forms.CharField(max_length=50, required=True, label="Nombre VLAN")
    vlan_tag = forms.IntegerField(required=True, label="VLAN TAG")
    vlan_desc = forms.CharField(max_length=60)

class OwnersForm(forms.Form):
    responsables_own = forms.CharField(max_length=50, required=True, label="Responsable")
    proyecto_own = forms.CharField(max_length=50, required=True, label="Proyecto")
    contacto_own = forms.CharField(max_length=50, required=True, label="Contacto")

class TorresOpsForm(forms.Form):
    operadores_ops = forms.CharField(max_length=50, required=True, label="Operador")
    team_ops = forms.CharField(max_length=50, required=True, label="Equipo")
    contacto_ops = forms.CharField(max_length=50, required=True, label="Contacto")