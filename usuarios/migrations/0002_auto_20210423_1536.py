# Generated by Django 2.2.19 on 2021-04-23 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Empleado',
            new_name='Usuario',
        ),
    ]