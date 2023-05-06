from rest_framework import serializers
from .models import Room


class RoomSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
