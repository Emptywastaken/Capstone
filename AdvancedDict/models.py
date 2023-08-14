from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.
from . import languageCodes

class diff_choices(models.IntegerChoices):
    EASY = 3, 'Easy'
    NORMAL = 6, 'Normal'
    HARD = 10, 'Hard'
    
class User(AbstractUser):
    pass

class NewWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField("New Word", max_length=50)
    translation = models.CharField("Translation", max_length=500)
    translation_edited = models.CharField("Displayed translation", max_length=500)
    sourceLanguage = models.CharField("Source language",max_length=5, choices=languageCodes.languages, default="en")
    targetLanguage = models.CharField("Target language",max_length=5, choices=languageCodes.languages, default="en")
    timestamp = models.DateTimeField(default=datetime.now())
    
    
    def __str__(self) -> str:
        return f'{self.sourceLanguage} {self.text} to {self.targetLanguage} {self.translation}'

class Quiz(models.Model):
    
 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    difficulty = models.IntegerField("Difficulty", choices=diff_choices.choices, default=diff_choices.EASY)
    score = models.PositiveIntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(default=datetime.now())
    questions = models.ManyToManyField(NewWord, related_name="quiz")
    answers = models.ManyToManyField("Answer", related_name="quiz")

    def __str__(self) -> str:
        return f'{self.user} got {self.score} at {self.timestamp.strftime("%d %B %Y %H:%M")}' 
    
    class Meta:
        verbose_name_plural = "Quizes"




    
class Answer(models.Model):
    text = models.CharField("User's answer", max_length=50)
    correct = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.quiz.get()} quiz answered {self.text}'
