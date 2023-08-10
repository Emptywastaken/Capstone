from django.contrib import admin

from .models import User, NewWord 
# Register your models here.

admin.site.register(User)
admin.site.register(NewWord)