from django import forms
from .models import Administrador

class AdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields = '__all__'
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'nombre_negocio': forms.TextInput(attrs={'class': 'form-control'}),
            'nit_rut': forms.TextInput(attrs={'class': 'form-control'}),
        }
