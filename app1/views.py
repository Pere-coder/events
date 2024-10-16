from django.shortcuts import render
from .models import Events
from .serializers import EventsSerializer
from rest_framework.generics import  ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.utils import timezone
# Create your views here.

class EventsListCreateAPIView(ListCreateAPIView):
    serializer_class = EventsSerializer

    def get_queryset(self):
        now = timezone.now()
        return Events.objects.filter(date__gte=now).order_by('-date')
    

    

class EventsDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer



