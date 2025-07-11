from django.contrib import admin
from .models import MyMessage

@admin.register(MyMessage)
class MyMessageAdmin(admin.ModelAdmin):
    list_display = ['id','sender','receiver','created_at']
