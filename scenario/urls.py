from django.urls import path
from . import views

app_name = 'scenario'

urlpatterns = [
    path('', views.scenario_list, name='scenario_list'),
]

