# Generated by Django 4.0.5 on 2022-06-10 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directorio', '0002_alter_persona_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='area',
            field=models.CharField(choices=[('Sistemas', 'Sistemas'), ('Tesorería', 'Tesorería'), ('Crédito', 'Crédito'), ('Dirección General', 'Dirección General'), ('Economía', 'Economía'), ('Negocio', 'Negocio'), ('Aseguramiento', 'Aseguramiento')], help_text='Entre el área a la que pertenece', max_length=50, verbose_name='Área'),
        ),
    ]