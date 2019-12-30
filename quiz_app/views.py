from django.shortcuts import render, redirect, reverse, get_object_or_404
from urllib.parse import urlencode
from django.contrib import messages
from .models import Quiz, Question, Answer

# Create your views here.
def home(request):
    return render(request, 'base.html')

def discover(request):
    all_quiz = Quiz.objects.all()
    return render(request, 'discover.html', {'all_quiz' : all_quiz})

def quiz(request, qname):
    quiz_obj = Quiz.objects.get(q_name = qname)
    return render(request, 'quiz.html', {'quiz_obj' : quiz_obj})

def basic_quest(request, quiz_name, slug):
    if request.method == "POST":
        guess = request.POST.get('answer')
        if guess == None:
            messages.warning(request,("Please Select An Answer Before Submitting!"))
            return redirect('basic_quest', quiz_name, slug)
        ans = Answer.objects.get(text = guess)
        if ans.is_correct == True:
            messages.info(request,("Well Done!"))
            return redirect('basic_quest', quiz_name, slug)
        else:
            messages.warning(request,("Wrong, Please Try Again!"))
            return redirect('basic_quest', quiz_name, slug)
    else:
        quest = slug.replace("-"," ") + "?"
        question = Question.objects.get(label = quest)
        answers = Answer.objects.filter(question = question.id)
        return render(request, 'quest.html', {'question' : question, 'answers' : answers})
