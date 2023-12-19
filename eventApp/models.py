from django.db import models

class Event(models.Model):
    # Campo para el título del evento con una longitud máxima de 255 caracteres
    title = models.CharField(max_length=255)
    
    # Campo para la descripción del evento (texto sin límite de longitud)
    description = models.TextField()
    
    # Campo para la fecha y hora de inicio del evento
    start_date = models.DateTimeField()
    
    # Campo para la fecha y hora de finalización del evento
    end_date = models.DateTimeField()
    
    # Campo para la ubicación del evento con una longitud máxima de 255 caracteres
    venue = models.CharField(max_length=255)

    class Meta:
        # Especifica la etiqueta de la aplicación a la que pertenece este modelo
        app_label = 'eventApp'