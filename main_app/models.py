from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField
from django.contrib.auth.models import User
from django.conf import settings
import requests, json 

GOOG_KEY = getattr(settings, "GOOG_KEY", None)


class Activity(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=100)
  date = models.DateField()
  duration = models.DurationField()
  start = models.TimeField()
  location = models.CharField(max_length=255)
  attendees = ArrayField((models.IntegerField()))
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'activity_id': self.id})

  class Meta:
        verbose_name_plural = "activities"

class Proposal(models.Model):
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  suggestion = models.CharField(max_length=255)
  location = location = models.CharField(max_length=255)
