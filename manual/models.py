from abc import ABC
from django.db import models

# Create your models here.

class Documento(models.Model):
    titulo = models.CharField('Título', max_length=50,
                              blank=True, help_text='Nombre del documento de texto')
    descripcion = models.CharField('Descripción', max_length=200,
                                   help_text='Detalle una breve descripción del contenido de la Instrucción', blank=True, null=True)
    anno = models.IntegerField(
        'Año de emisión', help_text='Año en que fue emitida')
    numero = models.IntegerField('Número', help_text='Número que le corresponde')
    archivo = models.FileField(
        'Archivo', upload_to='documentos/', max_length=50, help_text='Archivo a subir', blank=True, null=True)
    
    def __str__(self):
        return f"{self.titulo}"
    
    class Meta:
        abstract = True


class Biblioteca(models.Model):
    """Destinado a documentos importantes que se desean agregar al repositorio de documentos"""
    SHIRT_AREA = (
        ('Sistemas', 'Sistemas'),
        ('Tesorería', 'Tesorería'),
        ('Crédito', 'Crédito'),
        ('Direción General', 'Dirección General'),
        ('Economía', 'Economía'),
        ('Negocio', 'Negocio'),
        ('Aseguramiento', 'Aseguramiento'),
    )
    objects = models.Manager()
    nombre = models.CharField('Nombre', max_length=50)
    categoria = models.CharField('Categoría', max_length=200, help_text='Seleccione a que área pertenece el documento',
                                 choices=SHIRT_AREA)
    archivo = models.FileField('Comprimido', upload_to='biblioteca/', max_length=50,
                           help_text='Dirección del comprimido', blank=True, null=True)

    class Meta:
        verbose_name = 'Biblioteca'
        verbose_name_plural = 'Bibliotecas'

    def __str__(self):
        return f"{self.nombre}"


class Instruc(Documento):
    """las instrucciones seran buscadas por anno y tema,
    los temas solo pueden ser Credito, Economia, Tesoreria
    """
    objects = models.Manager()
    SHIRT_TEMA = (
        ('Crédito', 'Crédito'),
        ('Economía', 'Economía'),
        ('Tesorerí', 'Tesorería'),
    )
    tipo = models.CharField('Tipo de Instrucción',
                            max_length=50, help_text="Tipo de Intrucción")

    anexo = models.CharField('Anexo', max_length=50,
                             help_text='Defina el nombre de los anexos')
    tema = models.CharField('Tema', max_length=200, help_text='Defina a que área esta asociado este Tema',
                            choices=SHIRT_TEMA)

    class Meta:
        """Meta definicion para la clase asistencia"""
        verbose_name = 'Instrucción'
        verbose_name_plural = 'Instrucciones'

class Procedimiento(Documento):
    """ cuando sea buscado:
    por seccion solo pueden ser: 100, 200,300, 600, 700, 900
    en vez de por nombre por palabra
    por grupo y subgrupo
    """
    objects = models.Manager()
    SHIRT_SECCION = (
        ('100', '100'),
        ('200', '200'),
        ('300', '300'),
        ('600', '600'),
        ('700', '700'),
        ('900', '900'),
    )
    seccion = models.IntegerField(
        'Sección', help_text='Defina la sección a la que pertenece', choices=SHIRT_SECCION)
    grupo = models.CharField('Grupo', max_length=200,
                             help_text='Defina al grupo al que pertenece')
    subGrupo = models.CharField(
        'Subgrupo', max_length=50, help_text='Defina el subgrupo al que pertenece')
    anexo = models.CharField('Anexo', max_length=50,
                             help_text='Defina el nombre del anexo')
    proforma = models.CharField(
        'Proforma', max_length=50, help_text='Defina la proforma')

    class Meta:
        """Meta definicion para la clase asistencia"""
        verbose_name = 'Procedimiento'
        verbose_name_plural = 'Procedimientos'

class Circular(Documento):
    """Definición de las circulares"""
    objects = models.Manager()
    organismo = models.CharField(
        'Organismo emisor', max_length=20, help_text='Organismo Emisor')

    class Meta:
        """Meta definicion para la clase asistencia"""
        verbose_name = 'Circular'
        verbose_name_plural = 'Circulares'

    
