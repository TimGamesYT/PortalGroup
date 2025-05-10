from tracemalloc import get_object_traceback

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import ResponseForm


# Create your views here.

def question_list(request):
    questions = Question.objects.all()
    return render(request, "survey/survey.html", {"questions": questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = ResponseForm(question, request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            Answer.objects.create(
            question=question,
            answer_text=form.cleaned_data['answer'])
            return redirect("survey")

    return render(request, 'survey/question_detail.html', {'question': question, 'form': form})
