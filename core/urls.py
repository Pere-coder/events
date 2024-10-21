"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from app1.views import EventsListCreateAPIView, EventsDetailAPIView, EventsList, EventsCreate,EventsDetailView, EventsDeleteView, EventsUpdateView,CustomLoginView, GistListCreateAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', EventsListCreateAPIView.as_view(), name='events-list-create'),  
    path('events/<int:pk>/', EventsDetailAPIView.as_view(), name='events-detail'),
    path('', EventsList.as_view(), name='events-list'),
    path('events_create/', EventsCreate.as_view(), name='events-create'),   
    path('events_details/<int:pk>/', EventsDetailView.as_view(), name='events-details'), 
    path('events_update/<int:pk>/', EventsUpdateView.as_view(), name='events-update'),
    path('events_delete/<int:pk>/', EventsDeleteView.as_view(), name='events-delete'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('gist/', GistListCreateAPIView.as_view(), name='gist'),   
]
