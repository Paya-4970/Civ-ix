from django.shortcuts import render, redirect
from .models import MyMessage
from MyUser.models import MyUser
from .forms import MyMessageForm
from django.db import models


def send_message(request, username):
    user = request.user
    other_user = MyUser.objects.get(username = username)
    
    messages = MyMessage.objects.filter(
        (models.Q(sender=user) & models.Q(receiver=other_user)) |
        (models.Q(sender=other_user) & models.Q(receiver=user))
    ).order_by('created_at')
    
    if request.method == 'POST':
        form = MyMessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = user
            message.receiver = other_user
            message.save()

    else:
        form = MyMessageForm(initial={'receiver': other_user})
        
    return render(request, 'message/chat.html', {'messages': messages, 'form': form, 'other_user': other_user})

