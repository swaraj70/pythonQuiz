from django.shortcuts import render
from .models import Quiz

# Create your views here.
def home(request):
    return render(request, 'base.html')

def discover(request):
    all_quiz = Quiz.objects.all()
    return render(request, 'discover.html', {'all_quiz' : all_quiz})

def quiz(request, qname):
    quiz_obj = Quiz.objects.get(q_name = qname)
    return render(request, 'quiz.html', {'quiz_obj' : quiz_obj})