from django import forms
from .models import Vote, MySession, Participant

class MySessionForm(forms.ModelForm):
    class Meta:
        model = MySession
        fields = ['title','description']
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['role','user']

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['decision_option']
        
        