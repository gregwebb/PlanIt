from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Activity, Proposal

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''

  if request.method == "POST":
    pass
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
  

class ActivityCreate(LoginRequiredMixin, CreateView):
  model = Activity
  fields = ['name', 'date', 'duration', 'start', 'location', 'attendees']

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  fields = ['name', 'date', 'duration', 'start', 'location', 'attendees']

class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url = '/activities/'

def home(request):
  return render(request, 'home.html')

def activities_index(request):
  activities = Activity.objects.all()
  return render(request, 'activities/index.html', { 'activities': activities })

def activities_detail(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  return render(request, 'activities/detail.html', {
    'activity': activity
  })