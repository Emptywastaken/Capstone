from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.
from . import languageCodes

class diff_choices(models.IntegerChoices):
    EASY = 0, 'EASY'
    NORMAL = 1, 'Normal'
    HARD = 2, 'HARD'
    
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
    score = models.PositiveIntegerField(blank=True)
    timestamp = models.DateTimeField(default=datetime.now())

    def __str__(self) -> str:
        return f'{self.user} got {self.score}'


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(NewWord, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")
    

    def __str__(self) -> str:
        return f'{self.word}'

    
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="answer")
    text = models.CharField("User's answer", max_length=50)
    correct = models.BooleanField(default=False)
