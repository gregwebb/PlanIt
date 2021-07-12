from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Activity

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''

  if request.method == "POST":
    form = UserCreationForm(request.POST)

    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid Signup = Try Again!'

  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)
  

def home(request):
  return render(request, 'home.html')
