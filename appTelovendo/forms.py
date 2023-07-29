from .models import *
from appTelovendo.models import  Proveedor
from django import forms



class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre','email', 'telefono','productos']
        labels = {
            'nombre': 'Nombre del Proveedor',
            'email' : 'Correo elctronico',
            'telefono' : 'Numero Telefonico',
            'productos': 'Productos que ofreces'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'productos': forms.TextInput(attrs={'class': 'form-control'}),
        }
