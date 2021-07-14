from django import forms
from django.forms import ModelForm
from .models import Proposal, Activity

from django.forms.widgets import TextInput
from django.utils.dateparse import parse_duration


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'category', 'date', 'duration', 'start', 'location', 'attendees']
        widgets = {
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}),
            'duration': forms.TextInput(attrs={'placeholder': '00 day 00:00:00'}),
            'start': forms.TimeInput(attrs={'type': 'time'}),
        }

class ProposalForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['suggestion', 'location']