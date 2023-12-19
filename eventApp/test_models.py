from django.test import TestCase
from eventApp.models import Event

class EventModelTest(TestCase):
    # Prueba para verificar la creación de un evento
    def test_create_event(self):
        # Crea un evento de prueba
        event = Event.objects.create(
            title="Prueba",
            description="Descripcion de prueba",
            start_date="2023-01-01T12:00:00Z",
            end_date="2023-01-02T12:00:00Z",
            venue="Ubicacion de prueba"
        )

        # Verifica que los atributos del evento coincidan con los valores proporcionados
        self.assertEqual(event.title, "Prueba")
        self.assertEqual(event.description, "Descripcion de prueba")