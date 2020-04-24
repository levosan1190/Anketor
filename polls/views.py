from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice
from django.http import HttpResponse, HttpResponseRedirect


# pools index
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/polls_index.html', context)


# get questions
def q_index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}

    return render(request, 'polls/question_index.html', context)


# get specific questions and its result
def detail(request, question_id):
    if question_id not in list(Question.objects.filter().values_list('id', flat=True)):
        HttpResponse(f"{question_id} numaralı soru bulunamamıştır", status=404)

    question = Question.objects.get(pk=question_id)
    choices = Choice.objects.filter(question_id=question_id)
    context = {"question": question, "choices_list": choices}

    return render(request, 'polls/question_index.html', context=context)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {"question": question})


def vote(request, question_id, choice_id):
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=choice_id)

    choice.votes += 1
    choice.save()

    return render(request, 'polls/results.html', {'question': question})
