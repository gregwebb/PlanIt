from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField
from django.contrib.auth.models import User
from django.conf import settings
from django import forms

from functools import partial
DateInput = partial(forms.DateInput, {'class': 'datepicker'})

class Activity(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=100)
  date = models.DateField()
  duration = models.DurationField()
  start = models.TimeField()
  location = models.CharField(max_length=255)
  attendees = models.ManyToManyField(User, related_name='attend_user')
  user = models.ForeignKey(User, related_name='user_FK', on_delete=models.CASCADE)
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'activity_id': self.id})

  class Meta:
        verbose_name_plural = "activities"

class Proposal(models.Model):
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  suggestion = models.CharField(max_length=255)
  location = location = models.CharField(max_length=255)
  begin = ArrayField(models.DateTimeField(), blank=True, null=True)
  finish = ArrayField(models.DateTimeField(), blank=True, null=True)

class Comment(models.Model):
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.CharField(max_length=255)
  created = models.DateTimeField(auto_now_add=True)
