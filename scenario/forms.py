from django import forms
from .models import Scenario, Role, DecisionOption

class ScenarioForm(forms.ModelForm):
    class Meta:
        model = Scenario
        fields = ['title', 'description']

class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['name','description']

class DecisionOptionForm(forms.ModelForm):
    class Meta:
        model = DecisionOption
        fields = ['title', 'description']
