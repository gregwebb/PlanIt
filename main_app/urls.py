from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    # path('about/', views.about, name='about'),
    path('activities/', views.activities_index, name='index'), 
    path('activities/<int:activity_id>/', views.activities_detail, name='detail'), 
    path('activities/create/', views.ActivityCreate.as_view(), name='activities_create'),
    path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activities_update'),
    path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),
    # path('activities/<int:activity_id>/assoc_proposal/<int:proposal_id>/', views.assoc_proposal, name='assoc_proposal'),
    # path('activities/<int:activity_id>/unassoc_proposal/<int:proposal_id>/', views.unassoc_proposal, name='unassoc_proposal'),
    # path('proposals/', views.ProposalList.as_view(), name='proposals_index'),
    # path('proposals/<int:pk>/', views.ProposalDetail.as_view(), name='proposals_detail'),
    # path('proposals/create/', views.ToyCreate.as_view(), name='proposals_create'),
    # path('proposals/<int:pk>/update/', views.ProposalUpdate.as_view(), name='proposals_update'),
    # path('proposals/<int:pk>/delete/', views.ProposalDelete.as_view(), name='proposals_delete'),
    path('accounts/signup', views.signup, name='signup'), 
]