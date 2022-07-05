from importlib.util import module_from_spec
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User 

# Definicion de una persona
class Persona(models.Model):
    """define los atributos de una persona
    es importante que este relacionado con el metodo autenticar de la admin 
    """
    SHIRT_AREA = (
        ('Sistemas', 'Sistemas'),
        ('Tesorería', 'Tesorería'),
        ('Crédito', 'Crédito'),
        ('Dirección General', 'Dirección General'),
        ('Economía', 'Economía'),
        ('Negocio', 'Negocio'),
        ('Aseguramiento', 'Aseguramiento'),
    )
    objects = models.Manager()
    nombre = models.CharField('Nombre', max_length=50, help_text= 'Entre el nombre')
    apellidos = models.CharField('Apellidos',max_length=50, help_text= 'Entre el apellido')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50, default='Prueba', null=True) 
    area = models.CharField('Área', max_length=50, help_text='Entre el área a la que pertenece', choices = SHIRT_AREA) 
    cargo = models.CharField('Cargo', max_length=50, help_text='Entre el cargo que ocupa', blank=True, null=True)
    ext_telef = models.CharField('Extención de Teléfono', max_length=3,blank=True, help_text='Entre la extención telefónica')
    telef_dir = models.CharField('Telefono Directo', max_length=8, blank=True, help_text='Entre el número de teléfono directo')
    correo = models.EmailField('Correo', help_text= 'Entre la dirección de correo', blank=True, null=True)
    carnet = models.CharField('Carnet de identidad', max_length=11, help_text='Entre el número de carnet de identidad')
    cumple = models.DateField('Cumpleaños', help_text='Seleccione en el calendario su cumpleaños')
    # foto = models.ImageField(upload_to = None, height_field = None, width_field = None, max_length = 100)
    
    class Meta:
        """Meta definicion para la clase asistencia"""
        verbose_name = 'Personal de FINTUR'
        verbose_name_plural = 'Personal de FINTUR'
    
    def __str__(self):
        return f"nombre={self.nombre}"
  

class Centro_Externo(models.Model):
    """esta relacionado con los centros externos a la entidad"""
    objects = models.Manager()
    nombreEntidad = models.CharField('Nombre de la entidad', max_length=50, help_text='Nombre de la Entidad', blank=True, null=True)
    direccion =models.CharField('Dirección', max_length=100, help_text='Entre la dirección', blank=True, null=True)
    encargado = models.CharField('Encargado', max_length=50, help_text='Entre el nombre y apellidos del encargado', blank=True, null=True)
    area = models.CharField('Área', max_length=50, help_text='Área a la que pertenece', blank=True, null=True)
    categoria = models.CharField('Categoría', max_length=50, help_text='Defina la categoría', blank=True, null=True)
    supervisor = models.CharField('Supervisor',max_length=50, help_text='Supervisor del área', blank=True, null=True)
    telefono = models.CharField('Numero de teléfono',max_length=8, help_text='Registre el número de teléfono', blank=True, null=True)
    
    class Meta:
        """Meta definicion para la clase asistencia"""
        verbose_name = 'Centros Externos a la Entidad'
        verbose_name_plural = 'Centros Externos a la Entidad'

    def __srt__(self):
        return f"nombreEntidad={self.nombreEntidad}"

class OtrosEspacios(models.Model):
    nombre = models.CharField('Nombre', max_length=200, help_text='Nombre del área')
    telef = models.IntegerField('Número de Teléfono', help_text='Numero de teléfono')
    
    class Meta:
        verbose_name = 'Área Común'
        verbose_name_plural = 'Areas Comunes'
    
    def __str__(self):
        return f"nombre={self.nombre}"
    
    

   