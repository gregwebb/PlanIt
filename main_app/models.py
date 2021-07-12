from django.db import models
from django.contrib.postgres.fields import ArrayField

class Activity(models.Model):
  name = models.CharField(max_length=255)
  category = models.CharField(max_length=100)
  date = models.DateField()
  duration = models.DurationField()
  start = models.TimeField()
  location = models.CharField(max_length=255)
  attendees = ArrayField(ArrayField(models.IntegerField()))
  
  class Meta:
        verbose_name_plural = "activities"
