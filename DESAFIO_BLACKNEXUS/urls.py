from django.contrib import admin
from django.urls import path, include
from eventApp.views import EventListCreateView, EventDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', EventListCreateView.as_view(), name='event-list'),
    path('events/<int:pk>/', EventDetailView.as_view(), name='event-detail'),
    # Otras rutas del proyecto...
]