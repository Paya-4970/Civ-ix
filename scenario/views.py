from django.shortcuts import render, redirect
from .models import Scenario
from .forms import RoleForm, ScenarioForm, DecisionOptionForm
from MyUser.models import MyUser
from decorators.is_main import if_is_main

def scenario_list(request):
    scenarios = Scenario.objects.filter(is_active=True)
    context = {
        'scenarios': scenarios
    }
    return render(request, 'scenario/scenario_list.html', context)

@if_is_main
def add_scenario(request):
    if request.method == 'POST':
        form = ScenarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = ScenarioForm()

    return render(request, 'scenario/scenario-form.html', {'form': form})

@if_is_main
def add_role(request):
    if request.method == 'POST':
       form = RoleForm(request.POST)
       if form.is_valid():
           form.save()   
    else:
        form = RoleForm()
        
    return render(request, 'scenario/role-form.html',{'form':form})