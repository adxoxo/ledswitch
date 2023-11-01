from rest_framework import serializers
from .models import LedSTATE

class LedStateSerializer(serializers.Serializer):
    is_on = serializers.BooleanField()
    