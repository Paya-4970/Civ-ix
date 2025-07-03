from django.shortcuts import render
from .models import MySession

def mysession_list(request):
    sessions = MySession.objects.filter(is_active=True)
    context = {
        'sessions':sessions
    }
    return render(request, 'MySession/sessions_list.html',context)