from django.urls import path
from . import views

app_name = 'MyMessages'

urlpatterns = [
    path('chatroom/<str:username>/', views.send_message, name='chat'),
]
