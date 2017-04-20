from django.conf.urls import url
from quora.views import QuestionsList, AnswersList
from .import views

urlpatterns = [
    url(r'^$', QuestionsList.as_view(), name='questions'),
    url(r'^(?P<pk>[0-9]+)$', AnswersList.as_view(), name='answers'),
    url(r'^ask/$', views.question_view, name='ask'),
    url(r'^(?P<pk>[0-9]+)/answer/$', views.answer_view, name='answer'),

]
