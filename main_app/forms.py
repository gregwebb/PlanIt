# from typing_extensions import Required
from django import forms
from django.forms import ModelForm
from django.forms import widgets
from .models import Proposal, Activity, Comment

from django.forms.widgets import TextInput


class ActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields = ['name', 'category', 'date', 'start', 'stop', 'location',]
        labels = {
          'name': ('Name of activity:'),
          'category': ('Category of activity:'),
          'date': ('Date of activity'),
          'start': ('Starting time'),
          'stop': ('Ending time'),
          'location': ('Where are you thinking of having location?'),
    }
        widgets = {
            'date': forms.DateInput(format=('%m-%d-%Y'), attrs={'firstDay': 1, 'pattern=': '\d{2}-\d{2}-\d{4}', 'lang': 'pl', 'format': 'mm-dd-YYYY', 'type': 'date'},),
            'start': forms.TimeInput(attrs={'type': 'time'}),
            'stop': forms.TimeInput(attrs={'type': 'time'}),
        }

class ProposalForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['begin', 'finish', 'location', 'suggestion']
    labels = {
      'begin': ('Start Time:'),
      'finish': ('End Time:'),
      'location': (''),
      'suggestion': (''),
    }
    widgets = {
      'begin': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'},format='%Y-%m-%dT%H:%M'),
      'finish': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'},format='%Y-%m-%dT%H:%M'),
      'suggestion': forms.Textarea(attrs={"rows":2, 'placeholder':'add any additional info here', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'}),
      'location': forms.Textarea(attrs={"rows":2,'placeholder':'add location preference here - helpful to include city ', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'})
    }

class ProposalUpdateForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['location', 'suggestion']
    labels = {
      'location': (''),
      'suggestion': (''),
    }
    widgets = {
      'suggestion': forms.Textarea(attrs={"rows":2, 'placeholder':'add any additional info here - will replace existing info', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'}),
      'location': forms.Textarea(attrs={"rows":2,'placeholder':'update location preference here - helpful to include city ', 'style': 'border-radius: 30px', 'class': 'proposal-text-box'})
    }

class ProposalUpdateTimeForm(ModelForm):
  class Meta:
    model = Proposal
    fields = ['begin', 'finish']
    labels = {
      'begin': ('Start Time:'),
      'finish': ('End Time:')
    }
    widgets = {
      'begin': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'},format='%Y-%m-%dT%H:%M'),
      'finish': forms.DateTimeInput(attrs={'type': 'datetime-local','class': 'form-control'},format='%Y-%m-%dT%H:%M')
    }

class CommentForm(ModelForm):
  class Meta:
    model = Comment
    fields = ['content']
    labels = {
      'content': ('')
    }
    widgets = {
      'content': forms.Textarea(attrs={"rows":5, 'placeholder':'type comment here', 'style': 'border-radius: 30px', 'class': 'comment-text-box'}),
    } 
