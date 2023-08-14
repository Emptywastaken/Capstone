from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("quiz/new", views.generate_quiz, name="generate quiz"),
    path("quiz/<int:quiz_id>", views.get_quiz, name="display quiz"),
    path("quiz/report/<int:quiz_id>", views.report_quiz, name="report quiz"),

    #API
    path("edit/<int:word_id>", views.edit, name="edit"),

]