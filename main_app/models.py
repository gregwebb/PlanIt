from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField
from django.contrib.auth.models import User

import requests, json 

class Activity(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=100)
  date = models.DateField()
  duration = models.DurationField()
  start = models.TimeField()
  location = models.CharField(max_length=255)
  attendees = ArrayField((models.IntegerField()))
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'activity_id': self.id})

  class Meta:
        verbose_name_plural = "activities"

class Proposal(models.Model):
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  suggestion = models.CharField(max_length=255)
  location = location = models.CharField(max_length=255)

  def save(self, *args, **kwargs):
    loc = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?&address={self.location}&key=AIzaSyBrIZS88lbLzf3Nqecz_MVpaOpa7xzTWIA')
    data = json.loads(loc.text)['results']
    self.location = f"{data[0]['geometry']['location']['lat']}, {data[0]['geometry']['location']['lng']}"
    super().save(*args, **kwargs)


