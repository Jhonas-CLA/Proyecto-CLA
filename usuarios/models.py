from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager, Group, Permission

class MyAccountManager(BaseUserManager):
    def create_user(self, nombre_completo, username, email, password=None):
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico válido')
        if not username:
            raise ValueError('El usuario debe tener un nombre de usuario')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            nombre_completo=nombre_completo,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, nombre_completo, username, email, password):
        user = self.create_user(
            email=email,
            username=username,
            nombre_completo=nombre_completo,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superadmin = True
        user.is_active = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    nombre_completo = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    groups = models.ManyToManyField(
        Group,
        related_name='usuarios_usuario_groups',
        blank=True,
        help_text='Los grupos a los que pertenece este usuario.',
        verbose_name='groups',
        related_query_name='usuario',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuarios_usuario_permissions',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='user permissions',
        related_query_name='usuario',
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nombre_completo']

    objects = MyAccountManager()
    
    def __str__(self):
        return self.nombre_completo

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name_plural = "Usuarios"
