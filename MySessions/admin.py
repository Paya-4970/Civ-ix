from django.contrib import admin
from .models import MySession, Participant, Vote

@admin.register(MySession)
class MySessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'scenario', 'created_at', 'updated_at', 'is_active')
    list_filter = ('user', 'scenario', 'is_active')
    search_fields = ('title', 'user__username', 'scenario__title')
    list_per_page = 10  
        
@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'session', 'joined_at', 'is_active')
    list_filter = ('user', 'role', 'session', 'is_active')
    search_fields = ('user__username', 'role__name', 'session__title')
    list_per_page = 10
    
@admin.register(Vote)
class VoteAdmin(admin.ModelAdmin):
    list_display = ('participant', 'decision_option', 'created_at', 'updated_at', 'is_active')
    list_filter = ('participant', 'decision_option', 'is_active')
    search_fields = ('participant__user__username', 'decision_option__title')
    list_per_page = 10
    
    


