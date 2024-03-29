import datetime
from tabnanny import verbose
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
  question_text = models.CharField(max_length=200)
  publicated_at = models.DateTimeField("date published")

  class Meta:
    ordering = ["publicated_at"]
    # verbose_name_plural = "Preguntas"

  def __str__(self) -> str:
    return self.question_text
  
  def was_published_recently(self):
    return self.publicated_at >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
  
  def __str__(self) -> str:
    return self.choice_text
