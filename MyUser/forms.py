from django import forms
from django.core.exceptions import ValidationError
from MyUser.models import MyUser

class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = MyUser
        fields = ['username', 'phone', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm = cleaned_data.get("confirm_password")
        if password != confirm:
            raise ValidationError("Passwords do not match.")

class LoginForm(forms.Form):
    phone = forms.CharField(label="phone")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)