from django import forms
from .models import Answer
from django.forms.widgets import RadioSelect

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Answer
        CHOICES = [x for x in Answer.objects.filter(question = 1)]
        text = forms.ChoiceField(choices=CHOICES, required=True, widget = RadioSelect)
        fields = ['question', 'text', 'is_correct'] 