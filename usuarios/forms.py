from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    nombre_completo = forms.CharField(
        max_length=100,
        required=True,
        label="Nombre Completo",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Ingresa tu nombre completo'
        })
    )
    email = forms.EmailField(
        required=True,
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Ingresa tu email'
        })
    )

    username = forms.CharField(
        required=True,
        label="Nombre de Usuario",
    )

    password1 = forms.CharField(
        required=True,
        label="Contraseña",
    )

    password2 = forms.CharField(
        required=True,
        label="Confirma la contraseña",
    )

    class Meta:
        model = User
        fields = ['username', 'nombre_completo', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control form-control-lg'

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['nombre_completo']
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    usuario = forms.CharField(label='Usuario', max_length=100)
    contrasena = forms.CharField(label='Contraseña', widget=forms.PasswordInput)