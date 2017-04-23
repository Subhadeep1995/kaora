from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    question_text = forms.CharField(max_length=1000, label='')
    class Meta:
        model = Question
        fields = ['question_text',]

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields =['answer_text',]

