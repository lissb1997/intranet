# Generated by Django 4.0.5 on 2022-07-04 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0002_persona_hola'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='hola',
        ),
    ]