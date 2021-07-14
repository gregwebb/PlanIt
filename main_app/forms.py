from django import forms
from django.forms import ModelForm
from .models import Proposal, Activity, Comment

from django.forms.widgets import TextInput

class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'category', 'date', 'duration', 'start', 'location', 'attendees']
        widgets = {
            'date': forms.DateInput(format=('%d-%m-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{4}-\d{2}-\d{2}', 'lang': 'pl', 'format': 'yyyy-mm-dd', 'type': 'date'}),
            'duration': TextInput(attrs={'placeholder': '00 day 00:00:00'}),
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'attendees': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super(ActivityForm, self).__init__(*args, **kwargs)
        self.fields['attendees'].required = False

class ProposalForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['location', 'suggestion']
    labels = {
      'location': ('Where would you like to go? / What area are you going to be at?: (Include City)'),
      'suggestion': ('Add any additional info here:'),
    }

class ProposalUpdateForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['location', 'suggestion']
    labels = {
      'location': ('Where would you like to go? / What area are you going to be at?: (Include City)'),
      'suggestion': ('Add any additional info here:'),
    }

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']