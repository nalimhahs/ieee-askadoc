from django.urls import path

from .views import *


urlpatterns = [
    path('', homePageView, name='home'),
    path('ask', CreateQuestionView.as_view(), name='ask'),
    path('<slug:slug>/answer', answerView, name='answer'),
    path('<slug:slug>', detailView, name='detail'),
]
