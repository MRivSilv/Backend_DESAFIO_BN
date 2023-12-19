from django.test import TestCase
from eventApp.serializers import EventSerializer
class EventSerializerTest(TestCase):
    # Prueba para verificar el funcionamiento del serializador de eventos
    def test_event_serializer(self):
        # Datos de prueba para un evento
        data = {
            "title": "Serializer Test",
            "description": "Descripcion de prueba",
            "start_date": "2023-03-01T12:00:00Z",
            "end_date": "2023-03-02T12:00:00Z",
            "venue": "Serializer Test ubicacion"
        }

        # Crear una instancia del serializador con los datos de prueba
        serializer = EventSerializer(data=data)

        # Verificar que el serializador es válido
        self.assertTrue(serializer.is_valid())