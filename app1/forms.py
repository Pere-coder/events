from django import forms
from .models import Events


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ['link', 'date', 'description']  # Specify your fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['link'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget = forms.TextInput(attrs={'class': 'form-control datepicker'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})