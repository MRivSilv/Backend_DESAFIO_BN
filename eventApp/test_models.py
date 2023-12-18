from django.test import TestCase
from eventApp.models import Event

class EventModelTest(TestCase):
    def test_create_event(self):
        event = Event.objects.create(
            title="Prueba",
            description="Descripcion de prueba",
            start_date="2023-01-01T12:00:00Z",
            end_date="2023-01-02T12:00:00Z",
            venue="Ubicacion de prueba"
        )
        self.assertEqual(event.title, "Prueba")
        self.assertEqual(event.description, "Descripcion de prueba")
