from django.shortcuts import render
from .models import Events, Gist
from .serializers import EventsSerializer, GistSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView
from django.utils import timezone
from.forms import EventsForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class GistListCreateAPIView(ListAPIView, CreateAPIView):
    serializer_class = GistSerializer

    def get_queryset(self):
        now = timezone.now()
        return Gist.objects.filter(created_at__gte=now).order_by('-created_at')


class GistList(LoginRequiredMixin,ListView):
    model = Gist
    template_name = 'gist.html'
    context_object_name = 'gists'
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

class GistDelete(LoginRequiredMixin, DeleteView):
    model = Gist
    template_name = 'gist_confirm_delete.html'  # Create this template
    context_object_name = 'gists'
    success_url = reverse_lazy('gist-list')
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'



class EventsListCreateAPIView(ListAPIView):
    serializer_class = EventsSerializer

    def get_queryset(self):
        now = timezone.now()
        return Events.objects.filter(date__gte=now).order_by('-date')
    

    

class EventsDetailAPIView(LoginRequiredMixin, RetrieveAPIView):
    queryset = Events.objects.all()
    serializer_class = EventsSerializer
    


class EventsList(LoginRequiredMixin, ListView):
    model = Events
    template_name = 'events_list.html'
    context_object_name = 'events'
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

class EventsCreate(LoginRequiredMixin, CreateView):
    model = Events
    form_class = EventsForm
    template_name = 'events_create.html'
    success_url = reverse_lazy('events-list')
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'


class EventsDetailView(LoginRequiredMixin, DetailView):
    model = Events
    template_name = 'events_detail.html'
    context_object_name = 'event'
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

class EventsUpdateView(LoginRequiredMixin, UpdateView):
    model = Events
    form_class = EventsForm
    template_name = 'events_update.html'  # Create this template
    context_object_name = 'event'
    success_url = reverse_lazy('events-list')
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'

class EventsDeleteView(LoginRequiredMixin,DeleteView):
    model = Events
    template_name = 'events_confirm_delete.html'  # Create this template
    context_object_name = 'event'
    success_url = reverse_lazy('events-list')
    login_url = reverse_lazy('login')
    redirect_field_name = 'next'


class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = 'True'
    next_page = reverse_lazy('events-list')