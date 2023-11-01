from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import status
from .models import LedSTATE
from .serializers import LedStateSerializer

class LedSTATEView(ViewSet):

    def switchstateget(self, request):
        state, created = LedSTATE.objects.get_or_create()
        is_on = state.is_on
        serializer = LedStateSerializer({
            'is_on': is_on
        })
        led = serializer.data['is_on']
        return Response({
            led
        })


    def switchstate(self, request, format=None):

        serializer = LedStateSerializer(data=request.data)

        if serializer.is_valid():
            is_on = serializer.validated_data['is_on']
            led_state, created = LedSTATE.objects.get_or_create()
            led_state.is_on = is_on
            led_state.save()
            return Response ({
                'message': 'LED State updated successfully'
            })
        else:
            return Response(serializer.errors, status=400)

# Create your views here.
