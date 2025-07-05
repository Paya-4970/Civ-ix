from django.db import models
from MyUser.models import MyUser
from scenario.models import Role, Scenario, DecisionOption


class MySession(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    scenario = models.ForeignKey(Scenario, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    outcome = models.ForeignKey(DecisionOption,on_delete=models.SET_NULL,null=True,blank=True,related_name='sessions_outcome')
    
    def __str__(self):
        return f'{self.user.username} - {self.scenario.title}'

class Participant(models.Model):
    session = models.ForeignKey(MySession, on_delete=models.CASCADE, related_name='participant')
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} - {self.role.name}'
    
class Vote(models.Model):
    # session = models.ForeignKey(MySession, on_delete=models.CASCADE, null=True)
    participant = models.ForeignKey(Participant, on_delete=models.CASCADE)
    decision_option = models.ForeignKey(DecisionOption, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        unique_together = ('participant', 'decision_option')
        
    def __str__(self):
        return f'{self.participant.user.username} - {self.decision_option.title}'
    
    
    
