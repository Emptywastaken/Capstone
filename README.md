# Web personal dictionary with quizzes

## Distinctiveness and Complexity

### Distinctiveness
My project fulfills the distinctiveness requirement as it is an online dictionary with quizzes feature. 
There are no links to either an auction, social network, or online delivery website.

### Complexity
This project is more complex than any of these that are part of CS50W.
Complexity underlies in these features:
- Translation API to which request is made, utilizing json and request built-in python modules
- Edit, translation, and delete features are implemented with ajax using JavaScript
- In order to display the country flag custom template filter is created and loaded to templates that display flags.
- Questions for quizzes are randomly chosen, and quantity of questions correlates with the chosen difficulty
- Each answer is checked, check feature is user-friendly (in a case when there are multiple words with the same translation, if user's answer fits any of these, it's deemed correct)
- Quiz score evaluation
- Display reports for all finished quizzes
- Created complex models relationship including models with choice options.
- Use of Model forms
- Using .env file to not reveal private API_KEY

## Models

### NewWord model
- Basic fields user, timestamp
- CharFields that contain word information: text(word in source language), translation(word in target language) and translation edited (by default same as translation, changed in case word is edited later). sourceLanguage and targetLanguage are also charFields with choices argument that contains a list of all supported languages. 
- Has __str\_\_ method

### Quiz model

- Questions and answers are many-to-many fields that connects quiz to words(questions) and answers
- Difficulty field, used to determine amount of questions, has choices arg with models.InetegerChoices 
- Score, field to show how many question user answered correctly, Null in case quiz wasn't submitted.
- Basic fields user, timestamp
- __str\_\_ method
- Added Meta class to change "Quizs" to "Quizzes" in the admin site.

### Answer model

- text char field that contains the answer itself
- question foreign field that connects answer with respective question
- correct boolean field, false by default. Changed to true in case answer.text is correct
- __str\_\_ method

## JavaScript

Edit, translation, and delete buttons that are visible on each added word are all using js. Edit and delete buttons imply ajax requests. Translation button adds default translation which is useful in case user edited that word. JavaScript is also used in \<script\> tag of quizReport.html in order to give red background color to questions answered wrong

## Files

### App files(LanguageLearningTool/AdvancedDict)

- migrations folder contains all migrations
- static/AdvancedDict contatins styles.css that's used to change css of some elements, and words.js is a Javascript file that contains edit, translation and delete features.

- templates/AdvancedDict

    - index.html template for default view that has a form to post a new word, and all words list with paginator
    - layout.html template contains header and links to bootstrap, static files, etc., layout.html is used as layout for other templates
    - login.html template that displays a login form
    - register.html template that displays register form
    - newQuiz.html template that displays form where user chooses quiz difficulty. And then is redirected to a quiz.
    - quizDisplay.html template that displays questions and form for the answer, questions are changed using paginator
    - quizReport.html template that shows how many answers were correct
    - allReports.html template that displays reports for all completed quizzes

- templatetags
    - __init\_\_.py empty initialization file(it's required for custom templates tags to work according to django documentation)
    - tags_extra.py contains a custom django templates filter

- __init\_\_.py
- .env (this file is not present in git commits), used to store the API key for translation API
- admin.py contains models that are visible on admin site
- apps.py configures this app
- languageCodes.py Contains list of all supported languages, languages codes to country codes dictionary. And all info about languages and countries.
- models.py Contains django models
- tests.py Empty file was created on app initialization
- urls.py Contains app routes
- views.py Has django views that are assigned to different urls, also modelForms, API key is also loaded in this file

### Django project default files
These files are left untouched, they are created by initializing the project
- manage.py

- All files in the LanguageLearningTool/LanguageLearningTool folder

- LanguageLearningTool/LanguageLearningTool/settings.py contains project settings.

### Other files
- .gitignore Contains list of file extensions and files. So files with these extensions don’t get submitted with git commit.

- db.sqlite3(this file is not present in git commits). Project's database.
- requirements.txt packages that have to be installed in order to be able to run this web application

## How to run application

1. Install required pacages

2. Subscribe to this [API (it's free)](https://rapidapi.com/dickyagustin/api/text-translator2)

3. Get your X-RapidAPI-Key

4. Create .env file add API_KEY=INSERT_YOUR_API_KEY_HERE

5. Run python manage.py migrate

6. Run python manage.py runserver

7. Register new user
