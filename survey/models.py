from django.db import models


# Create your models here.
# QUESTION_CHOICES = [('text', 'Text'),
#                     ('choice', 'Choice'),

#                         ]
# class Question(models.Model):
    
#     text = models.CharField(max_length=200)

#     question_type = models.CharField(max_length=20, choices=QUESTION_CHOICES, default='text')

#     def __str__(self):
#         return self.text


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200)

#     def __str__(self):
#         return self.text


# class Response(models.Model):
#    question = models.ForeignKey(Question, on_delete=models.CASCADE)
#    user_response = models.TextField()
#    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True, blank=True)

#    def __str__(self):
#        return f"Response to {self.question.text}"

class Question(models.Model):
    TEXT = 'text'
    CHOICE = 'choice'
    QUESTION_TYPES = [
        (TEXT, 'Text'),
        (CHOICE, 'Choice'),
    ]

    text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    choices = models.TextField(blank=True, help_text="USE COMA")

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    submitted_at = models.DateTimeField(auto_now_add=True)