from django.contrib import admin
from .models import Scenario, DecisionOption, Role

@admin.register(Scenario)
class ScenarioAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    
@admin.register(DecisionOption)
class DecisionOptionAdmin(admin.ModelAdmin):
    list_display = ('scenario', 'title', 'description', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    list_editable = ('is_active',)
    
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('scenario', 'name', 'description', 'created_at', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'description')
    list_editable = ('is_active',)
    
    


    
