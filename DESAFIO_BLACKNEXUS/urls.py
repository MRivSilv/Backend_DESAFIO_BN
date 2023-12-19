from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from eventApp.views import EventListCreateView, EventDetailView


urlpatterns = [
    # URL para acceder a la interfaz de administrador de Django
    path('admin/', admin.site.urls),

    # URL raíz (''), redirige a la vista de lista de eventos ('event-list')
    path('', RedirectView.as_view(pattern_name='event-list', permanent=False)),

    # URL para acceder a la vista de lista y creación de eventos
    path('events/', EventListCreateView.as_view(), name='event-list'),

    # URL para acceder a la vista de detalle, actualización y eliminación de eventos
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
]