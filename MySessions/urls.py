from django.urls import path
from . import views

app_name = 'MySession'

urlpatterns = [
    path('add/vote/<int:session>/', views.add_vote, name='vote-form'),
    path('session_list', views.mysession_list, name='session_list'),
    path('add/session', views.add_mysession, name='session-form'),
    path('add/participant', views.add_participant, name='participant-form'),
]

