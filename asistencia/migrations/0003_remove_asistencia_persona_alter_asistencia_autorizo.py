# Generated by Django 4.0.5 on 2022-06-12 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0002_alter_asistencia_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asistencia',
            name='persona',
        ),
        migrations.AlterField(
            model_name='asistencia',
            name='autorizo',
            field=models.BooleanField(blank=True, max_length=50, null=True),
        ),
    ]