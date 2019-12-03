from django.urls import path
from quiz_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('discover/', views.discover, name='discover'),
    path('quiz/', views.quiz, name='quiz'),
]