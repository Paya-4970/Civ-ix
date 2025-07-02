from django.shortcuts import render
from .models import Scenario

def scenario_list(request):
    scenarios = Scenario.objects.filter(is_active=True)
    context = {
        'scenarios': scenarios
    }
    return render(request, 'scenario/scenario_list.html', context)
