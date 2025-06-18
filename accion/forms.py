from django import forms
from .models import Administrador
from .models import Proveedor
from usuarios.models import Usuario

#Configuracion administrador

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

#Proveedor

class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del proveedor'}),
            'empresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre de la empresa'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }


#Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UsuarioForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            self.fields.pop('password')

        widgets = {
            'nombre_completo': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre completo del usuario'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Nombre de usuario'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Correo electrónico'
            }),
            'rol': forms.Select(attrs={
                'class': 'form-control'
            }),
        }