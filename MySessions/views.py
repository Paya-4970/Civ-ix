from django.shortcuts import render, redirect
from .models import MySession
from decorators.is_main import if_is_main
from .forms import VoteForm, ParticipantForm, MySessionForm

def mysession_list(request):
    sessions = MySession.objects.filter(is_active=True)
    context = {
        'sessions':sessions
    }
    return render(request, 'MySession/sessions_list.html',context)

@if_is_main
def add_mysession(request):
    user = request.user
    if request.method == 'POST':
        form = MySessionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('/')
    else:
        form = MySessionForm()
        
    return render(request,'MySession/session-form.html', {'form':form})
            
@if_is_main
def add_participant(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ParticipantForm()
        
    return render(request,'MySession/participant-form.html', {'form':form})
            
@if_is_main
def add_mysession(request):
    user = request.user
    if request.method == 'POST':
        form = MySessionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.save()
            return redirect('/')
    else:
        form = MySessionForm()
        
    return render(request,'MySession/session-form.html', {'form':form})
            
