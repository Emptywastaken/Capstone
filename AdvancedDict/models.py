from django.db import models
from django.contrib.auth.models import AbstractUser

from datetime import datetime
# Create your models here.
# from language_codes import languages

class User(AbstractUser):
    pass

class entry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.s("New Word", max_length=50)
    source_language = models.CharField("Source language code",max_length=5)
    target_language = models.CharField("Target language code",max_length=5)
    translation = models.CharField("Translation", max_length=50)
    

    