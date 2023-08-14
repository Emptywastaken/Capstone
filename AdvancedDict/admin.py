from django.contrib import admin

from .models import User, NewWord, Quiz, Answer
# Register your models here.

admin.site.register(User)
admin.site.register(NewWord)
admin.site.register(Answer)
admin.site.register(Quiz)