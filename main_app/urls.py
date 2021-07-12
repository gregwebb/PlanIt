from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    # path('about/', views.about, name='about'),
    # path('activities/', views.activities_index, name='index'), 
    # path('activities/<int:activity_id>/', views.activities_detail, name='detail'), 
    # path('activities/create/', views.ActivityCreate.as_view(), name='activities_create'),
    # path('activities/<int:pk>/update/', views.ActivityUpdate.as_view(), name='activities_update'),
    # path('activities/<int:pk>/delete/', views.ActivityDelete.as_view(), name='activities_delete'),
]