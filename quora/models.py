from django.db import models
from django.utils import timezone

class Question(models.Model):
    author = models.ForeignKey('auth.User')
    question_text = models.CharField(max_length=250)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField()
    answered_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.answer_text
