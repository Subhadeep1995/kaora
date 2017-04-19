from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView

from . models import Question, Answer

class QuestionsList(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'quora/question_list.html'

class AnswersList(DetailView):
    model = Question
    #context_object_name = 'answers'
    template_name = 'quora/answer_list.html'
