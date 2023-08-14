from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from django.db import IntegrityError

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse

from django import forms
from django.forms import ModelForm

from django.core.paginator import Paginator


from datetime import datetime

from .models import User, NewWord, Quiz, Answer
from . import languageCodes

import requests, os, json, random
from dotenv import load_dotenv
# export PYTHONPATH=c:/users/admin/appdata/local/programs/python/python311/lib/site-packages

load_dotenv()
API_KEY=os.getenv('API_KEY')


# Forms

class New_word(ModelForm):  
    class Meta:
        model = NewWord
        fields = ("text", "sourceLanguage", "targetLanguage",)
        
        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control", "maxlength": "50"}),
            "sourceLanguage": forms.Select(attrs={"class": "form-select"}),
            "targetLanguage": forms.Select(attrs={"class": "form-select"}),
        }

class New_quiz(ModelForm):
    class Meta:
        model = Quiz
        fields = ("difficulty",)

        widgets = {
            "difficulty": forms.Select(attrs={"class": "form-select form-select-lg"})
        }

class New_answer(ModelForm):
    class Meta:
        model = Answer
        fields = ("text",)

        widgets = {
            "text": forms.TextInput(attrs={"class": "form-control form-control-lg"})
        }

def index(request):
    if request.method =="POST":
        form = New_word(request.POST)
        if form.is_valid():

            new_word_form = form.save(commit=False)

            # Sending request to the API
            url = "https://text-translator2.p.rapidapi.com/translate"
            headers = {
                "content-type": "application/x-www-form-urlencoded",
                "X-RapidAPI-Key": API_KEY,
                "X-RapidAPI-Host": "text-translator2.p.rapidapi.com"
            }
            payload = {
                "source_language": new_word_form.sourceLanguage,
                "target_language": new_word_form.targetLanguage,
                "text": new_word_form.text,
                
            }
            
            response = requests.post(url, data=payload, headers=headers)
            new_word_form.timestamp = datetime.now() 
            new_word_form.translation = response.json()["data"]["translatedText"].lower()
            new_word_form.translation_edited = response.json()["data"]["translatedText"].lower()
            new_word_form.user = request.user
            new_word_form.text = new_word_form.text.lower()
            new_word_form.save()
            return HttpResponseRedirect(reverse('index'))

    else:
        words = NewWord.objects.filter(user = request.user).order_by('-timestamp')
        return render(request, "AdvancedDict/index.html", {
            "form": New_word,
            "words": words,
            "dict": languageCodes.languages_to_countries_dict,
            })

@csrf_exempt
@login_required
def generate_quiz(request):
    if request.method == "POST":
        form = New_quiz(request.POST)
        if form.is_valid:
            new_quiz_form = form.save(commit=False)
            new_quiz_form.timestamp = datetime.now(tz=None)
            new_quiz_form.user = request.user
            new_quiz_form.save()
            print(new_quiz_form.pk)
            return HttpResponseRedirect(f"{new_quiz_form.pk}")
    else:
        return render(request, "AdvancedDict/newQuiz.html", {
            "form": New_quiz
        })

@csrf_exempt
@login_required
def get_quiz(request, quiz_id):

    quiz = Quiz.objects.get(pk = quiz_id)

    if request.user != quiz.user:
        return HttpResponse(status=400)
    
    if request.method == "POST":    

        form = New_answer(request.POST)
        if form.is_valid:
            new_answer_form = form.save(commit=False)
            q_pk = request.POST.get("question")
            
            # Making quiz more user-friendly, so it checks if answer is correct for any words with same translation
            temp_word = NewWord.objects.get(pk = q_pk).translation_edited
            
            matching_values = NewWord.objects.filter(text=temp_word).values_list("text", flat=True)
            print(matching_values)
            if new_answer_form.text.lower() in list(matching_values):
                new_answer_form.correct = True
            new_answer_form.save()

            # linking answer to quiz
            quiz.answers.add(new_answer_form)
        # print(request.POST)
            page = int(request.POST.get("page", 1))
            print("page", page)

            if "final" in request.POST:
                # Updating quiz score onsubmit
                answers_score = sum(list(quiz.answers.all().values_list("correct", flat=True)))
                quiz.score = answers_score
                quiz.save()
                return HttpResponseRedirect(reverse("index"))
            return HttpResponseRedirect(reverse("display quiz", kwargs={"quiz_id": quiz_id}) + f"?page={page+1}")

        # if form is invalid
        else:
            return HttpResponse(status=400)
        
    else:    
        question_count = quiz.questions.all().count()
        # print("diff" ,quiz.difficulty)
        # print("count", question_count)
        if question_count != quiz.difficulty:
            words = NewWord.objects.values_list('pk', flat=True).filter(user = request.user)
            # words = NewWord.objects.filter(user = request.user)
            # print(words)
            for _ in range(quiz.difficulty):
                # print(random.choice(words))
                indx = random.choice(words)
                # words.exclude(indx)
                quiz.questions.add(NewWord.objects.get(pk = indx))

        p = Paginator(quiz.questions.all().order_by('pk'), 1)
        page = request.GET.get('page')
        page_obj = p.get_page(page)
        # print(quiz.questions.all())
        return render(request, "AdvancedDict/quizDisplay.html", {
            "quiz": quiz,
            "page": page_obj,
            "dict": languageCodes.languages_to_countries_dict,
            "form": New_answer
        })
     

@csrf_exempt
def edit(request, word_id):
    try: 
        word = NewWord.objects.get(pk = word_id)
    except NewWord.DoesNotExist:
        return JsonResponse({"error": "Word does not exist."}, status=404)
    
    # in case of attempt to access another user post
    if request.user != word.user:
        return JsonResponse({"error": "Cannot edit another user's word."}, status=404)
    
    if request.method == "PUT":
        data = json.loads(request.body) 
        if data.get("translation") is not None:
            word.translation_edited = data["translation"]
            word.save()
            return HttpResponse(status=204)
        else:
            return JsonResponse({"error": "Invalid request"}, status=400)

    elif request.method == "DELETE":
        word.delete()
        return HttpResponse(status=204)

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "AdvancedDict/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "AdvancedDict/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "AdvancedDict/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "AdvancedDict/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "AdvancedDict/register.html")