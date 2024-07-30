from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HostsForm(forms.Form):
    host_name = forms.CharField(max_length=50, required=True, label="Hostname")
    host_ip = forms.CharField(required=True, label="Direccion IP")
    host_vlan = forms.IntegerField(required=True, label="VLAN TAG")


class RegistroForm(UserCreationForm):
    username = forms.CharField(max_length=20, label="Usuario")
    first_name = forms.CharField(max_length=20, label="Nombre")
    last_name = forms.CharField(max_length=20, label="Apellido")
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]