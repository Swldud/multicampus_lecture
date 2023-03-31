from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe

from .models import Question
from .forms import QuestionForm


@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'GET':
        form = QuestionForm()

    else:
        form = QuestionForm(request.POST)
        if form.is_valid:
            question = form.save()
            return redirect('detail', question.pk)
        
    return render(request, 'qna/form.html', {
        'form': form
    })

@require_safe
def index(request):
    questions = Question.objects.all()
    return render(request, 'qna/index.html', {'questions': questions})


@require_safe
def detail(request, question_id):
    # question = Question.objects.get(pk = question_id)
    question = get_object_or_404(Question, pk = question_id)
    return render(request, 'qna/detail.html', {'question': question})


@require_http_methods(['GET', 'POST'])
def update(request, question_id):
    # question = Question.objects.get(pk =  question_id)
    question = get_object_or_404(Question, pk =question_id)

    if request.method == 'GET':
        form = QuestionForm(instance= question)
        
    elif request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            question = form.save()

            return redirect('detail', question.pk)

    return render(request, 'qna/form.html', {'form': form })


@require_POST
def delete(request, question_id):

    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk = question_id)

    question.delete()
    return redirect('index')


