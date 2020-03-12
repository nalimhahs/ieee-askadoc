from django.urls import reverse_lazy, path, reverse
from django.views.generic import CreateView, TemplateView
from django.db.models import Count, Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.shortcuts import get_object_or_404, redirect, render

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm


def homePageView(request):

    all_questions = Question.objects.all().order_by('-pub_date')
    query_set = []
    for question in all_questions:
        try:
            ans = Answer.objects.get(question=question)
            query_set.append((question, ans))
        except:
            query_set.append((question, None))

    return render(request, 'pages/index.html', {'questions': query_set})


def detailView(request, slug):
    
    question = Question.objects.get(slug=slug)
    try:
        answer = Answer.objects.get(question=question)
    except:
        answer = None

    return render(request, 'pages/detail.html', {'question': question, 'answer': answer, })



class CreateQuestionView(CreateView):

    template_name = 'pages/create-question.html'
    message = ('Thank you! your question has been created.')
    form_class = QuestionForm

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateQuestionView, self).form_valid(form)

    def get_success_url(self):
        return reverse('home')


def answerView(request, slug):
    
    question = Question.objects.get(slug=slug)
    try:
        answer = Answer.objects.get(question=question)
        return redirect('detail', slug=slug)
    except:
        answer = None

    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.user = request.user
            answer.question = question
            answer.save()
            return redirect('detail', slug=slug)

    else:
        form = AnswerForm()

    return render(request, 'pages/create-answer.html', {'question': question, 'answer': answer, 'form': form})

