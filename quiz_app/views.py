from django.shortcuts import render
from .models import Quiz

# Create your views here.
def home(request):
    return render(request, 'base.html')

def discover(request):
    return render(request, 'discover.html')

def quiz(request, quiz_id):
    quiz_obj = Quiz.objects.get(pk=quiz_id)
    return render(request, 'quiz.html', {'quiz_obj' : quiz_obj})