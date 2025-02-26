
from django import forms
from django.conf import settings
from .models import Question, Answer


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question',]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['answer',]
