# Generated by Django 4.0.5 on 2022-08-29 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asistencia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='vacaciones',
            field=models.DurationField(blank=True, help_text='Reserve los dias que desea de vacaciones', null=True, verbose_name='futuras Vacaciones'),
        ),
    ]
