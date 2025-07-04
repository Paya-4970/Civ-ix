from django.urls import path
from . import views

app_name = 'scenario'

urlpatterns = [
    path('', views.scenario_list, name='scenario_list'),
    path('add_form/', views.add_scenario, name='scenario_form'),
    path('add_role/', views.add_role, name='role_form'),
    path('add_decision/', views.add_decision_option, name='decision_form'),
]

