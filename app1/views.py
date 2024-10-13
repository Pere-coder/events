from django.shortcuts import render
from .models import Events
from .serializers import EventsSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.

class EventsListCreateAPIView(ListCreateAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

class EventsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer

