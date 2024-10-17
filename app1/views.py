from django.shortcuts import render
from .models import Events
from .serializers import EventsSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.utils import timezone
from.forms import EventsForm
from django.urls import reverse_lazy
# Create your views here.

class EventsListCreateAPIView(ListAPIView):
    serializer_class = EventsSerializer

    def get_queryset(self):
        now = timezone.now()
        return Events.objects.filter(date__gte=now).order_by('-date')
    

    

class EventsDetailAPIView(RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    


class EventsList(ListView):
    model = Events
    template_name = 'events_list.html'
    context_object_name = 'events'

class EventsCreate(CreateView):
    model = Events
    form_class = EventsForm
    template_name = 'events_create.html'
    success_url = reverse_lazy('events-list')


class EventsDetailView(DetailView):
    model = Events
    template_name = 'events_detail.html'
    context_object_name = 'event' 

class EventsUpdateView(UpdateView):
    model = Events
    form_class = EventsForm
    template_name = 'events_update.html'  # Create this template
    context_object_name = 'event'
    success_url = reverse_lazy('events-list')

class EventsDeleteView(DeleteView):
    model = Events
    template_name = 'events_confirm_delete.html'  # Create this template
    context_object_name = 'event'
    success_url = reverse_lazy('events-list') 

