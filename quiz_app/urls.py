from django.urls import path
from quiz_app import views

urlpatterns = [
    path('<quiz_id>', views.quiz, name='quiz')
]