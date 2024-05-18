
from django.urls import path
from .import views

urlpatterns = [
 
   path('quiz/', views.quiz, name= 'quiz'),
   path('get-quiz/', views.get_quiz, name='get_quiz')
 ]