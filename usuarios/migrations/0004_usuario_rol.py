# Generated by Django 5.2.1 on 2025-06-17 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_remove_usuario_date_joined_remove_usuario_groups_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('admin', 'Administrador'), ('usuario', 'Usuario')], default='usuario', max_length=20),
        ),
    ]
