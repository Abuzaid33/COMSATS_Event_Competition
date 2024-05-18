from django.urls import path
from ChatApp import views
urlpatterns = [
    path('Chat/', views.chat, name='Chatt'),
]
