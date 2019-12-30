from django.urls import path
from quiz_app import views

urlpatterns = [
    path('<qname>', views.quiz, name='quiz'),
    path('<quiz_name>/<slug:slug>', views.basic_quest, name='basic_quest'),
]

#[\w\s]+