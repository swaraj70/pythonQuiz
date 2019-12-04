from django.db import models

# Create your models here.

class Quiz(models.Model):
    q_name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.q_name