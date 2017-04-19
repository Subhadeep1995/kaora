from django.conf.urls import url
from quora.views import QuestionsList, AnswersList

urlpatterns = [
    url(r'^$', QuestionsList.as_view(), name='questions'),
    url(r'^(?P<pk>[0-9]+)$', AnswersList.as_view(), name='answers')

]
