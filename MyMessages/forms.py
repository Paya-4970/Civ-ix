from django import forms
from .models import MyMessage

class MyMessageForm(forms.ModelForm):
    class Meta:
        model = MyMessage
        fields = ['text']