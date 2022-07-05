from django.db import models
from django.contrib.auth.models import User 


# from django.forms import ValidationError
from directorio.models import Persona


class Asistencia(models.Model):
    """Definicion del modelo para la clase asistencia.
    la fecha la coge el sistema automaticamente
    se desea que el usuario solo ponga la hora
    las vacaciones deben salir como un campo para seleccionar inicio y fin o
    seleccionar cuando comienza y cuando termina
    el autorizo no debe ser modificado por el trabajador solo por el director asociado a ese trabajador
    el nombre debe ser cogido automaticamente del usuario con que se autentico
    """
    objects = models.Manager()
    fecha_actual = models.DateField(auto_now_add=True)
    hora_entrada_M = models.TimeField('Hora de Entrada', auto_now_add=False,
                                      help_text='Defina su hora de llegada a la entidad en el horario de la mañana')
    hora_salida_M = models.TimeField('Hora salida de la mañana', auto_now_add=False,
                                     help_text='Defina su horario de salida al almuerzo')
    hora_entrada_T = models.TimeField('Hora entrada de la tarde', auto_now_add=False,
                                      help_text='Defina su hora de entrada de la tarde')
    hora_salida_T = models.TimeField('Hora de salida de la tarde', auto_now_add=False,
                                     help_text='Defina su horario de salida de la entidad')
    # vacaciones = models.DurationField('futuras Vacaciones', null=True, blank=True,
    #                                   help_text='Reserve los dias que desea de vacaciones')
    # vacaciones_Inicio = models.DateField('Fecha de inicio de las futuras vacaciones',
    # null=True, blank=True, help_text='Defina a partir de que fecha desea vacaciones el próximo mes')
    # vacaciones_Fin = models.DateField('Fecha de las futuras vacaciones', blank=True,
    # null=True, help_text='Defina hasta que fecha desea vacaciones el próximo mes')
    autorizo = models.BooleanField(max_length=50, blank=True, null=True)  # arreglar
    observaciones = models.CharField('Observaciones', max_length=200, blank=True,
                                     help_text='Desea agregar algún comentario al Especialista de Recursos Humanos')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, max_length=50, default='Prueba')
 

    class Meta:
        """Meta definicion para la clase asistencia"""
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'

    def __str__(self):
        """Unicode que se desea mostrar de Asistencia"""
        return f"para {self.fecha_actual}"
