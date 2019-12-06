from django.urls import path
from quiz_app import views

urlpatterns = [
    path('<qname>', views.quiz, name='quiz')
]