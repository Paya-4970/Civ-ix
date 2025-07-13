from django.shortcuts import get_object_or_404, render, redirect
from .models import MySession, Participant, Vote
from decorators.is_main import if_is_main
from .forms import VoteForm, ParticipantForm, MySessionForm
from scenario.models import Scenario
from MyMessages.forms import MyMessageForm
from MyMessages.models import MyMessage


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



from django.shortcuts import get_object_or_404, redirect, render
from django.core.exceptions import ObjectDoesNotExist

def session_room(request, session_id):
    session = get_object_or_404(MySession, id=session_id)
    user = request.user

    participant, created = Participant.objects.get_or_create(session=session, user=user)

    messages = MyMessage.objects.filter(
        sender=user, receiver__in=session.participant_set.values_list('user', flat=True)
    ) | MyMessage.objects.filter(
        receiver=user, sender__in=session.participant_set.values_list('user', flat=True)
    )
    messages = messages.order_by('created_at')

    vote_form = VoteForm()
    message_form = MyMessageForm()

    # گرفتن رأی اگر قبلاً ثبت شده
    try:
        partic_vote = Vote.objects.get(participant=participant)
        already_voted = partic_vote.done
    except Vote.DoesNotExist:
        partic_vote = None
        already_voted = False

    if request.method == 'POST':
        if not already_voted and 'vote' in request.POST:
            vote_form = VoteForm(request.POST)
            if vote_form.is_valid():
                vote = vote_form.save(commit=False)
                vote.user = user
                vote.done = True
                vote.participant = participant
                vote.session = session
                vote.save()
                return redirect('MySession:session-room', session_id=session.id)

        elif 'message' in request.POST:
            message_form = MyMessageForm(request.POST)
            if message_form.is_valid():
                message = message_form.save(commit=False)
                message.sender = user
                # فرض بر اینکه پیام به یک participant دیگه هست؟ اگر نه، این خط باید تغییر کنه
                message.receiver = participant.user
                message.save()
                return redirect('MySession:session-room', session_id=session.id)

    return render(request, 'MySession/session-room.html', {
        'session': session,
        'participants': session.participant_set.select_related('user'),
        'messages': messages,
        'vote_form': vote_form,
        'already_voted':already_voted,
        'message_form': message_form
    })

            
