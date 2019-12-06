from django.db import models

# Create your models here.

class Quiz(models.Model):
    q_name = models.CharField(max_length=30)
    desc = models.CharField(max_length=100)
    
    def __str__(self):
        return self.q_name

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    label = models.CharField(max_length=1000)
    
    def __str__(self):
        return self.label
        
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=1000)
    is_correct = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text