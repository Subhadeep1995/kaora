from django.shortcuts import render, redirect, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView, DetailView
from .forms import QuestionForm, AnswerForm


from . models import Question, Answer

class QuestionsList(ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'quora/question_list.html'

class AnswersList(DetailView):
    model = Question
    #context_object_name = 'answers'
    template_name = 'quora/answer_list.html'

def question_view(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.published_date = timezone.now()
            question.save()
            return redirect('questions')
        else:
            message = 'please fill up the form correctly'
            form = QuestionForm
            return render(request, 'quora/ask.html', {'form': form, 'message':message})
    else:
        form = QuestionForm(None)
        return render(request, 'quora/ask.html', {'form':form})

def answer_view(request, pk):
    if request.method == 'POST':
        question = get_object_or_404(Question, pk=pk)
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.answered_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('answers', pk=pk)
        else:
            message = 'Please check the details'
            return render(request, 'quora/answer.html', {'form':form})
    else:
        form = AnswerForm(None)
        return render(request, 'quora/answer.html', {'form':form})