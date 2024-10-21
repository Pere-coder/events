from rest_framework import serializers
from .models import Events, Gist



class EventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'


class GistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gist
        fields = '__all__'