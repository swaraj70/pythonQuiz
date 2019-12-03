from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def discover(request):
    return render(request, 'discover.html')

def quiz(request):
    return render(request, 'quiz.html')