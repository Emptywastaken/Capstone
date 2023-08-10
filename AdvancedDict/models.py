from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.
from . import languageCodes

class User(AbstractUser):
    pass

class NewWord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField("New Word", max_length=50)
    translation = models.CharField("Translation", max_length=50)
    sourceLanguage = models.CharField("Source language",max_length=5, choices=languageCodes.languages, default="en")
    targetLanguage = models.CharField("Target language",max_length=5, choices=languageCodes.languages, default="en")
    timestamp = models.DateTimeField(default=datetime.now())


   