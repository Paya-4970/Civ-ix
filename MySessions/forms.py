from django import forms
from .models import Vote, MySession, Participant

class MySessionForm(forms.ModelForm):
    class Meta:
        model = MySession
        fields = ['scenario','title','description']
        

class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['decision_option']
        
        
class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['session','role','user']