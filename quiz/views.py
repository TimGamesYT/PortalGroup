from tracemalloc import get_object_traceback

from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import ResponseForm


# Create your views here.

def index(request):
    questions = Question.objects.all()
    return render(request, "quiz/quiz.html", {"questions": questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == "POST":
        form = ResponseForm(request.POST, question=question)
        if form.is_valid:
            response = form.save(commit=False)
            response.question = question
            response.save()
            return redirect("index")
    else:
        form = ResponseForm(question=question)

    return render(request, 'quiz/question_detail.html', {'question': question, 'form': form})
