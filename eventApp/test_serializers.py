from django.test import TestCase
from eventApp.serializers import EventSerializer
class EventSerializerTest(TestCase):
    def test_event_serializer(self):
        data = {
            "title": "Serializer Test",
            "description": "Descripcion de prueba",
            "start_date": "2023-03-01T12:00:00Z",
            "end_date": "2023-03-02T12:00:00Z",
            "venue": "Serializer Test ubicacion"
        }
        serializer = EventSerializer(data=data)
        self.assertTrue(serializer.is_valid())