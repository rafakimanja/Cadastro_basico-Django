# Generated by Django 4.2.1 on 2023-05-12 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_sistema_cadastro', '0002_rename_usuarios_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='name',
            new_name='nome',
        ),
    ]
