from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    # path('about/', views.about, name='about'),
    path('activities/', views.activities_index, name='index'), 
    path('activities/<int:activity_id>/', views.activities_detail, name='detail'), 
    path('activities/create/', views.create_activity, name="activities_create"),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activities_update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),
    # path('activities/<int:activity_id>/assoc_proposal/<int:proposal_id>/', views.assoc_proposal, name='assoc_proposal'),
    # path('activities/<int:activity_id>/unassoc_proposal/<int:proposal_id>/', views.unassoc_proposal, name='unassoc_proposal'),
    # path('proposals/', views.ProposalList.as_view(), name='proposals_index'),
    path('proposals/<int:proposal_id>/', views.proposals_detail, name='proposals_detail'),
    path('proposals/create/', views.ProposalCreate.as_view(), name='proposals_create'),
    path('activities/<int:activity_id>/add_proposal/', views.add_proposal, name='add_proposal'),
    path('activities/<int:activity_id>/update_proposal/', views.update_proposal, name='update_proposal'),
    # path('proposals/<int:pk>/update/', views.ProposalUpdate.as_view(), name='proposals_update'),
    # path('proposals/<int:pk>/delete/', views.ProposalDelete.as_view(), name='proposals_delete'),
    path('accounts/signup', views.signup, name='signup'), 
    path('activities/<int:activity_id>/add_comment/', views.add_comment, name='add_comment'),
    path('activities/<int:activity_id>/add_attendee/', views.add_attendee, name='add_attendee'),
    path('activities/<int:activity_id>/remove_attendee/', views.remove_attendee, name='remove_attendee'),
]