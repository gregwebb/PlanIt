from django import forms
from django.forms import ModelForm
from .models import Proposal, Activity

class ActivityForm(ModelForm):
    
    class Meta:
        model = Activity
        fields = ['name', 'category', 'date', 'duration', 'start', 'location', 'attendees']
        widgets = {
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}),
        }

class ProposalForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['suggestion', 'location']