from django.test import TestCase, Client
from django.urls import reverse
from eventApp.models import Event
from rest_framework import status
import json
class EventViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_events(self):
        # Crear algunos eventos de prueba
        Event.objects.create(title='Evento 1', description='Descripción del evento 1', start_date='2023-01-01T00:00:00Z', end_date='2023-01-02T00:00:00Z', venue='Lugar 1')
        Event.objects.create(title='Evento 2', description='Descripción del evento 2', start_date='2023-02-01T00:00:00Z', end_date='2023-02-02T00:00:00Z', venue='Lugar 2')

        # Realizar solicitud GET a la vista de lista de eventos
        response = self.client.get(reverse('event-list'))

        # Verificar que la solicitud sea exitosa (código 200)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Verificar que la respuesta contiene la información esperada
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]['title'], 'Evento 1')
        self.assertEqual(response.json()[1]['title'], 'Evento 2')

    def test_create_event_view(self):
        data = {
            "title": "Crear evento prueba",
            "description": "Descripcion de prueba",
            "start_date": "2023-02-01T12:00:00Z",
            "end_date": "2023-02-02T12:00:00Z",
            "venue": "Ubicacion de prueba"
        }
        response = self.client.post(reverse('event-list'), data=json.dumps(data), content_type='application/json')
        self.assertEqual(response.status_code, 201)