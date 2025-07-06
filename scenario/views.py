from django.shortcuts import render, redirect
from .models import Scenario
from .forms import RoleForm, ScenarioForm, DecisionOptionForm
from MyUser.models import MyUser
from decorators.is_main import if_is_main

def scenario_list(request, scenario_id=None):
    if scenario_id: 
        if request.user.is_main:
            scenarios = Scenario.objects.get(id=scenario_id)
            context = {
                'scenarios': scenarios
            }
            request.session['current_id_scenario'] = scenario_id
            session = request.session.get('current_id_scenario')
            # print(session)
            return render(request, 'scenario/scenario-details.html',context)
        else:
            return redirect('/')
    else:
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
    session = request.session.get('current_id_scenario')
    # print(session)
    if request.method == 'POST':
       scenario = Scenario.objects.get(id = session) 
    #    print(scenario.title)
       form = RoleForm(request.POST)
       if form.is_valid():
           role = form.save(commit=False)
           role.scenario = scenario
           role.save()
           return redirect('/')   
    else:
        form = RoleForm()
        
    return render(request, 'scenario/role-form.html',{'form':form})

@if_is_main
def add_decision_option(request):
    if request.method == 'POST':
       form = DecisionOptionForm(request.POST)
       if form.is_valid():
           form.save()   
           return redirect('/') 
    else:
        form = DecisionOptionForm()
        
    return render(request, 'scenario/decision-form.html',{'form':form})