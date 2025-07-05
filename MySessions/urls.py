from django.urls import path
from . import views

app_name = 'MySession'

urlpatterns = [
    path('session_list', views.mysession_list, name='session_list'),
    path('add/session', views.add_mysession, name='session-form'),
]

