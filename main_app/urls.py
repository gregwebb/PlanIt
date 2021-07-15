from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('activities/', views.activities_index, name='index'), 
    path('activities/<int:activity_id>/', views.activities_detail, name='detail'), 
    path('activities/create/', views.create_activity, name="activities_create"),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activities_update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),
    path('activities/<int:activity_id>/delete_proposal/', views.delete_proposal, name='proposals_delete'),
    path('proposals/<int:proposal_id>/', views.proposals_detail, name='proposals_detail'),
    path('proposals/create/', views.ProposalCreate.as_view(), name='proposals_create'),
    path('activities/<int:activity_id>/add_proposal/', views.add_proposal, name='add_proposal'),
    path('activities/<int:activity_id>/update_proposal/', views.update_proposal, name='update_proposal'),
    path('activities/<int:activity_id>/update_proposal_time/', views.update_proposal_time, name='update_proposal_time'),
    path('accounts/signup', views.signup, name='signup'), 
    path('activities/<int:activity_id>/add_comment/', views.add_comment, name='add_comment'),
    path('activities/<int:activity_id>/add_attendee/', views.add_attendee, name='add_attendee'),
    path('activities/<int:activity_id>/remove_attendee/', views.remove_attendee, name='remove_attendee'),
    path('my_lists/', views.my_list, name='my_list'),
]