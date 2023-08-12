from django.contrib import admin

from .models import User, NewWord, Quiz
# Register your models here.

admin.site.register(User)
admin.site.register(NewWord)
admin.site.register(Quiz)