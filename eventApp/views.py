from rest_framework import generics
from .models import Event
from .serializers import EventSerializer

class EventListCreateView(generics.ListCreateAPIView):
    # Establece el conjunto de consultas para todos los eventos
    queryset = Event.objects.all()
    # Establece el serializador a utilizar para la vista
    serializer_class = EventSerializer

# Clase que implementa una vista para recuperar, actualizar y destruir eventos
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    # Establece el conjunto de consultas para todos los eventos
    queryset = Event.objects.all()
    # Establece el serializador a utilizar para la vista
    serializer_class = EventSerializer