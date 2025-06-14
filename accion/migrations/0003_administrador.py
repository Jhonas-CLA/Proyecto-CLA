# Generated by Django 5.2.1 on 2025-06-13 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accion', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=100)),
                ('correo', models.EmailField(max_length=254, unique=True)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.TextField(blank=True, null=True)),
                ('nombre_negocio', models.CharField(max_length=100)),
                ('nit_rut', models.CharField(blank=True, max_length=20, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='logos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('actualizado', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
