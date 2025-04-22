from django.db import models


# Create your models here.

class Question(models.Model):
    text = models.CharField(max_length=200)
    question_type = models.CharField(max_length=20, choices=[('text', 'Text'), ('choice', 'Choice')])

    def __str__(self):
        return self.text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text


class Response(models.Model):
   question = models.ForeignKey(Question, on_delete=models.CASCADE)
   user_response = models.TextField()
   choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)

   def __str__(self):
       return f"Response to {self.question.text}"