from django import forms
from .models import Usuario
from django.contrib.auth.hashers import make_password

from django import forms
from django.contrib.auth.hashers import make_password
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    password1 = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Ingresa tu contraseña'})
    )
    password2 = forms.CharField(
        label='Confirmar contraseña',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirma tu contraseña'})
    )

    class Meta:
        model = Usuario
        fields = ['nombre_completo', 'username', 'email', 'rol', 'estado']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={'placeholder': 'Nombre completo'}),
            'username': forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Correo electrónico'}),
            'rol': forms.Select(attrs={'id': 'id_rol'}),
            'estado': forms.Select(attrs={'id': 'id_estado'}),
        }

    def clean_nombre_completo(self):
        nombre = self.cleaned_data.get("nombre_completo", "").strip()
        if len(nombre.split(' ')) < 2:
            raise forms.ValidationError("Debes ingresar nombre y apellido completos.")
        return nombre

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError('Este correo ya está registrado.')
        return email

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if Usuario.objects.filter(username=username).exists():
            raise forms.ValidationError('Este nombre de usuario ya está en uso.')
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Las contraseñas no coinciden.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password1'])  # Hashea la contraseña
        if commit:
            user.save()
        return user

