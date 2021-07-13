from django.db import models
from django.urls import reverse
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

class Activity(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=100)
  date = models.DateField()
  duration = models.DurationField()
  start = models.TimeField()
  location = models.CharField(max_length=255)
  attendees = ArrayField(ArrayField(models.IntegerField()))
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'activity_id': self.id})

  class Meta:
        verbose_name_plural = "activities"
