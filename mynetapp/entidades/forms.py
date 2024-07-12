from django import forms 

class HostsForm(forms.Form):
    host_name = forms.CharField(max_length=50, required=True, label="Hostname")
    host_ip = forms.CharField(required=True, label="Direccion IP")
    host_vlan = forms.IntegerField(required=True, label="VLAN TAG")



    