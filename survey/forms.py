from django import forms
from .models import Question

# class ResponseForm(forms.ModelForm):
#     class Meta:
#         model = Response
#         if Question.question_type == 'text':
#             fields = ['user_response']
#         else:
#         fields = ['choice']

#     def __init__(self, *args, **kwargs):
#         question = kwargs.pop('question')
#         super(ResponseForm, self).__init__(*args, **kwargs)
#         if question.question_type == 'choice':
#             self.fields['choice'].queryset = question.choice_set.all()
#         else:
#             del self.fields['choice']

class ResponseForm(forms.Form):
    def __init__(self, question: Question, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if question.question_type == Question.TEXT:
            self.fields['answer'] = forms.CharField(label=question.text)
        elif question.question_type == Question.CHOICE:
            choices = [(c.strip(), c.strip()) for c in question.choices.split(',')]
            self.fields['answer'] = forms.ChoiceField(label=question.text, choices=choices)