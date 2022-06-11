# Generated by Django 4.0.5 on 2022-06-08 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directorio', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_actual', models.DateField(auto_now_add=True)),
                ('hora_entrada_M', models.TimeField(help_text='Defina su hora de llegada a la entidad en el horario de la mañana', verbose_name='Hora de Entrada')),
                ('hora_salida_M', models.TimeField(help_text='Defina su horario de salida al almuerzo', verbose_name='Hora salida de la mañana')),
                ('hora_entrada_T', models.TimeField(help_text='Defina su hora de entrada de la tarde', verbose_name='Hora entrada de la tarde')),
                ('hora_salida_T', models.TimeField(help_text='Defina su horario de salida de la entidad', verbose_name='Hora de salida de la tarde')),
                ('vacaciones', models.DurationField(blank=True, help_text='Reserve los dias que desea de vacaciones', null=True, verbose_name='futuras Vacaciones')),
                ('autorizo', models.BooleanField(blank=True, max_length=50)),
                ('observaciones', models.CharField(blank=True, help_text='desea agregar algún comentario al Especialista de Recursos Humanos', max_length=200, verbose_name='Observaciones')),
                ('nombre', models.CharField(max_length=200)),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='directorio.persona')),
            ],
            options={
                'verbose_name': 'Registro de la asistencia',
                'verbose_name_plural': 'Registro de la asistencia',
            },
        ),
    ]
