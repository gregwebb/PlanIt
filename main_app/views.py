from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Activity, Proposal, Comment
from .forms import ActivityForm, ProposalForm, CommentForm, ProposalUpdateForm, ProposalUpdateTimeForm

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import requests, json
import os


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


def home(request):
    return render(request, 'home.html')


@login_required
def create_activity(request):
  form = ActivityForm(request.POST)
  if form.is_valid():
    google_key = os.environ['GOOGLE_KEY']
    new_activity = form.save(commit=False)
    new_activity.user = request.user
    new_activity.save()
    new_activity.attendees.add(request.user)
    initial_proposal = Proposal()
    initial_proposal.location = new_activity.location
    initial_proposal.activity = new_activity
    initial_proposal.user = request.user
    initial_proposal.begin = []
    initial_proposal.finish = []
    initial_proposal.begin.append(f'{new_activity.date} {new_activity.start}')
    initial_proposal.finish.append(f'{new_activity.date} {new_activity.stop}')
    initial_proposal.suggestion = f"I would like to have activity {new_activity.name} at {new_activity.location}."
    loc = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?&address={initial_proposal.location}&key={google_key}')
    data = json.loads(loc.text)['results']
    initial_proposal.location = f"{data[0]['geometry']['location']['lng']}, {data[0]['geometry']['location']['lat']}"
    initial_proposal.save()
    return redirect('detail', activity_id=new_activity.id)
    
  return render(request, 'main_app/activity_form.html', {
    'form': form
  })


def activities_index(request):
  activities = Activity.objects.all()
  return render(request, 'activities/index.html', { 'activities': activities })


def activities_detail(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  proposal_form = ProposalForm()
  proposal_update_form = ProposalUpdateForm()
  proposal_update_time_form = ProposalUpdateTimeForm()
  comment_form = CommentForm()
  proposals = Proposal.objects.filter(activity_id=activity_id)
  coors = []
  new_coors = []
  sum_lng = 0
  sum_lat = 0
  for proposal in proposals:
    coors.append(proposal.location)
  for item in coors:
    result = [x.strip() for x in item.split(',')]
    new_coors.append(result)
  for item in new_coors:
    sum_lng = sum_lng + float(item[0])
    sum_lat = sum_lat + float(item[1])
  if len(proposals)>0:
    center = f"{sum_lng/len(coors)}, {sum_lat/len(coors)}"
  else: 
    center = "-98.4842, 39.0119"
  if request.user.id:
    user_proposal = Proposal.objects.filter(activity_id=activity_id).filter(user=request.user)
  else:
    user_proposal = 0
  if request.user in activity.attendees.all():
    attending = True
  else: 
    attending = False
  return render(request, 'activities/detail.html', {
    'activity': activity, 
    'proposal_form': proposal_form, 
    'center': center, 
    'comment_form': comment_form, 
    'user_proposal': user_proposal,
    'proposal_update_form': proposal_update_form, 
    'proposal_update_time_form': proposal_update_time_form, 
    'attending': attending,
    'mapbox_key': os.environ.get('MAPBOX_KEY')    
  })


class ActivityUpdate(LoginRequiredMixin, UpdateView):
  model = Activity
  form_class = ActivityForm
  def form_valid(self, form):
    return super().form_valid(form)


class ActivityDelete(LoginRequiredMixin, DeleteView):
  model = Activity
  success_url = '/activities/'
def my_list(request):
  if request.user.is_authenticated:
    activities = Activity.objects.filter(user=request.user)
    return render(request, 'my_lists/my_list.html', { 'activities': activities })
  else:
    return render(request, 'home.html')


class ProposalCreate(LoginRequiredMixin, CreateView):
  model = Proposal
  fields = ['activity', 'user', 'suggestion', 'location']
  

def proposals_detail(request, proposal_id):
  proposal = Proposal.objects.get(id=proposal_id)
  return render(request, 'proposals/detail.html', {
    'proposal': proposal
  })


@login_required
def add_proposal(request, activity_id):
  form = ProposalForm(request.POST)
  if form.is_valid():
    google_key = os.environ['GOOGLE_KEY']
    new_proposal = form.save(commit=False)
    new_proposal.user = request.user
    new_proposal.activity_id = activity_id
    loc = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?&address={new_proposal.location}&key={google_key}')
    data = json.loads(loc.text)['results']
    new_proposal.location = f"{data[0]['geometry']['location']['lng']}, {data[0]['geometry']['location']['lat']}"
    new_proposal.save()
  return redirect('detail', activity_id=activity_id)


@login_required
def update_proposal(request, activity_id):
  form = ProposalUpdateForm(request.POST)
  if form.is_valid():
    google_key = os.environ['GOOGLE_KEY']    
    update_proposal = form.save(commit=False)
    existing_proposal = Proposal.objects.filter(activity_id=activity_id).filter(user=request.user).first()
    update_proposal.id = existing_proposal.id
    update_proposal.activity_id = activity_id
    update_proposal.user = request.user
    loc = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?&address={update_proposal.location}&key={google_key}')
    data = json.loads(loc.text)['results']
    update_proposal.location = f"{data[0]['geometry']['location']['lng']}, {data[0]['geometry']['location']['lat']}"
    update_proposal.begin = existing_proposal.begin
    update_proposal.finish = existing_proposal.finish
    update_proposal.save()
  return redirect('detail', activity_id=activity_id)


@login_required
def update_proposal_time(request, activity_id):
  form = ProposalUpdateTimeForm(request.POST)
  if form.is_valid():
    update_proposal = form.save(commit=False)
    existing_proposal = Proposal.objects.filter(activity_id=activity_id).filter(user=request.user).first()
    update_proposal.id = existing_proposal.id
    update_proposal.activity_id = activity_id
    update_proposal.user = request.user
    update_proposal.location = existing_proposal.location
    existing_proposal.begin.append(update_proposal.begin[0])
    existing_proposal.finish.append(update_proposal.finish[0])
    update_proposal.begin = existing_proposal.begin
    update_proposal.finish = existing_proposal.finish
    update_proposal.suggestion = existing_proposal.suggestion
    update_proposal.save()
  return redirect('detail', activity_id=activity_id)


def delete_proposal(request, activity_id):
    delete_proposal = Proposal.objects.filter(activity_id=activity_id).filter(user=request.user).first()
    delete_proposal.delete()
    return redirect('detail', activity_id=activity_id)


@login_required
def add_comment(request, activity_id):
  form = CommentForm(request.POST)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.user = request.user
    new_comment.activity_id = activity_id
    new_comment.save()
  return redirect('detail', activity_id=activity_id)


def my_list(request):
  if request.user.is_authenticated:
    activities = Activity.objects.filter(user=request.user)
    return render(request, 'my_lists/my_list.html', { 'activities': activities })
  else:
    return render(request, 'home.html')


@login_required
def add_attendee(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  if activity.attendees.all().filter(username=request.user) != True:
    activity.attendees.add(request.user)
  else:
    pass
  return redirect('detail', activity_id=activity_id)


@login_required
def remove_attendee(request, activity_id):
  activity = Activity.objects.get(id=activity_id)
  activity.attendees.remove(request.user)

  return redirect('detail', activity_id=activity_id)


class SearchResultsView(ListView):
  model = Activity
  template_name = 'search_results.html'
  
  def get_queryset(self):
    query = self.request.GET.get('q')
    object_list = Activity.objects.filter(name__icontains=query)
    return object_list