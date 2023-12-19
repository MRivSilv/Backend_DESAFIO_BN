from rest_framework import serializers
from .models import Event

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        # Especifica el modelo que el serializador va a manejar
        model = Event
        # Especifica los campos que se deben incluir en la serialización (todos en este caso)
        fields = '__all__'