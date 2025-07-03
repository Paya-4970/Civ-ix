from django.shortcuts import render, redirect
from .models import Scenario
from .forms import RoleForm, ScenarioForm, DecisionOptionForm
from MyUser.models import MyUser

def scenario_list(request):
    scenarios = Scenario.objects.filter(is_active=True)
    context = {
        'scenarios': scenarios
    }
    return render(request, 'scenario/scenario_list.html', context)


def add_scenario(request):
    user = request.user
    if not user.is_main:
        return redirect('/')  

    if request.method == 'POST':
        form = ScenarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  
    else:
        form = ScenarioForm()

    return render(request, 'scenario/scenario-form.html', {'form': form})