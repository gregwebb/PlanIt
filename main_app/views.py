from django.shortcuts import render
from django.http import HttpResponse
from .models import Activity


def home(request):
  return render(request, 'home.html')
