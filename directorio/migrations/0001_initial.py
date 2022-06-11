# Generated by Django 4.0.5 on 2022-06-10 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_Externo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreEntidad', models.CharField(blank=True, help_text='Nombre de la Entidad', max_length=50, null=True, verbose_name='Nombre de la entidad')),
                ('direccion', models.CharField(blank=True, help_text='Entre la dirección', max_length=100, null=True, verbose_name='Dirección')),
                ('encargado', models.CharField(blank=True, help_text='Entre el nombre y apellidos del encargado', max_length=50, null=True, verbose_name='Encargado')),
                ('area', models.CharField(blank=True, help_text='Área a la que pertenece', max_length=50, null=True, verbose_name='Área')),
                ('categoria', models.CharField(blank=True, help_text='Defina la categoría', max_length=50, null=True, verbose_name='Categoría')),
                ('supervisor', models.CharField(blank=True, help_text='Supervisor del área', max_length=50, null=True, verbose_name='Supervisor')),
                ('telefono', models.CharField(blank=True, help_text='Registre el número de teléfono', max_length=8, null=True, verbose_name='Numero de teléfono')),
            ],
            options={
                'verbose_name': 'Centros Externos a la Entidad',
                'verbose_name_plural': 'Centros Externos a la Entidad',
            },
        ),
        migrations.CreateModel(
            name='OtrosEspacios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Nombre del área', max_length=200, verbose_name='Nombre')),
                ('telef', models.IntegerField(help_text='Numero de teléfono', verbose_name='Número de Teléfono')),
            ],
            options={
                'verbose_name': 'Área Común',
                'verbose_name_plural': 'Areas Comunes',
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Entre el nombre', max_length=50, verbose_name='Nombre')),
                ('apellidos', models.CharField(help_text='Entre el apellido', max_length=50, verbose_name='Apellidos')),
                ('usuario', models.CharField(blank=True, help_text='Entre el usuario', max_length=10, null=True, verbose_name='Usuario')),
                ('area', models.CharField(choices=[('S', 'Sistemas'), ('T', 'Tesorería'), ('C', 'Crédito'), ('D', 'Dirección General'), ('E', 'Economía'), ('N', 'Negocio'), ('A', 'Aseguramiento')], help_text='Entre el área a la que pertenece', max_length=50, verbose_name='Área')),
                ('cargo', models.CharField(blank=True, help_text='Entre el cargo que ocupa', max_length=50, null=True, verbose_name='Cargo')),
                ('ext_telef', models.CharField(blank=True, help_text='Entre la extención telefónica', max_length=3, verbose_name='Extención de Teléfono')),
                ('telef_dir', models.CharField(blank=True, help_text='Entre el número de teléfono directo', max_length=8, verbose_name='Telefono Directo')),
                ('correo', models.EmailField(blank=True, help_text='Entre la dirección de correo', max_length=254, null=True, verbose_name='Correo')),
                ('carnet', models.CharField(help_text='Entre el número de carnet de identidad', max_length=11, verbose_name='Carnet de identidad')),
                ('cumple', models.DateField(help_text='Seleccione en el calendario su cumpleaños', verbose_name='Cumpleaños')),
            ],
            options={
                'verbose_name': 'Personal de FINTUR',
                'verbose_name_plural': 'Personal de FINTUR',
            },
        ),
    ]
