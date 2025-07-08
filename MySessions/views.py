from django.shortcuts import render, redirect
from .models import MySession, Participant
from decorators.is_main import if_is_main
from .forms import VoteForm, ParticipantForm, MySessionForm
from scenario.models import Scenario


def mysession_list(request, session_id=None):
    if session_id:
        request.session['current_session_id'] = session_id
        sessions = MySession.objects.get(is_active=True, id = session_id)
        context = {
            'sessions':sessions
        }
        return render(request, 'MySession/sessions-by-id.html',context)
    else:
        sessions = MySession.objects.filter(is_active=True).order_by('-created_at')
        context = {
            'sessions':sessions
        }
        return render(request, 'MySession/sessions_list.html',context)

@if_is_main
def add_mysession(request):
    user = request.user
    session = request.session.get('current_id_scenario')
    scenario = Scenario.objects.get(id = session)
    if request.method == 'POST':
        form = MySessionForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = user
            form.scenario = scenario
            form.save()
            return redirect('/')
    else:
        form = MySessionForm()
        
    return render(request,'MySession/session-form.html', {'form':form})
            
@if_is_main
def add_participant(request):
    session = request.session.get('current_session_id')
    my_session = MySession.objects.get(id = session)
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            participant = form.save(commit=False)
            participant.session = my_session
            participant.save()
            return redirect('/')
    else:
        form = ParticipantForm()
        
    return render(request,'MySession/participant-form.html', {'form':form})
            
@if_is_main
def add_vote(request, session):
    user = request.user
    participant = Participant.objects.get(session_id = session, user=user)
    if request.method == 'POST':
        form = VoteForm(request.POST)
        if form.is_valid():
            vote = form.save(commit=False)
            vote.participant = participant
            vote.save()
            return redirect('/')
    else:
        form = VoteForm()
        
    return render(request,'MySession/vote-form.html', {'form':form})
    
            
