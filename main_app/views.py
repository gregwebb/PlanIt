from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Activity, Proposal

from .forms import ActivityForm, ProposalForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.conf import settings

import requests, json

GOOG_KEY = getattr(settings, "GOOG_KEY", None)

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


@login_required
def create_activity(request):
  activity_form = ActivityForm(request.POST)
  if activity_form.is_valid():
    activity_form.save()
    return redirect('index')

  return render(request, 'main_app/activity_form.html', {
    'activity_form': activity_form
  })

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
  proposal_form = ProposalForm()
  return render(request, 'activities/detail.html', {
    'activity': activity, 'proposal_form': proposal_form
  })

class ProposalCreate(LoginRequiredMixin, CreateView):
  model = Proposal
  fields = ['activity', 'user', 'suggestion', 'location']
  
def proposals_detail(request, proposal_id):
  proposal = Proposal.objects.get(id=proposal_id)
  return render(request, 'proposals/detail.html', {
    'proposal': proposal
  })

def add_proposal(request, activity_id):
  form = ProposalForm(request.POST)
  if form.is_valid():
    new_proposal = form.save(commit=False)
    new_proposal.user = request.user
    new_proposal.activity_id = activity_id
    loc = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?&address={new_proposal.location}&key={GOOG_KEY}')
    data = json.loads(loc.text)['results']
    new_proposal.location = f"{data[0]['geometry']['location']['lat']}, {data[0]['geometry']['location']['lng']}"
    new_proposal.save()
  return redirect('detail', activity_id=activity_id)