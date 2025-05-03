from django import forms
from .models import Question, Response

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['user_response', 'choice']

    def __init__(self, *args, **kwargs):
        question = kwargs.pop('question')
        super(ResponseForm, self).__init__(*args, **kwargs)
        if question.question_type == 'choice':
            self.fields['choice'].queryset = question.choice_set.all()
        else:
            del self.fields['choice']
