from django.urls import path
from quiz_app import views

urlpatterns = [
    path('<qname>', views.quiz, name='quiz'),
    path('<quiz_name>/<ques_no>', views.basic_quest, name='basic_quest'),
]