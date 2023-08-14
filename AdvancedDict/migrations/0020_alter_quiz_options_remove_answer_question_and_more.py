# Generated by Django 4.2.3 on 2023-08-14 11:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AdvancedDict", "0019_remove_newword_quiz_quiz_questions_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="quiz",
            options={"verbose_name_plural": "Quizes"},
        ),
        migrations.RemoveField(
            model_name="answer",
            name="question",
        ),
        migrations.RemoveField(
            model_name="answer",
            name="user",
        ),
        migrations.AddField(
            model_name="quiz",
            name="answers",
            field=models.ManyToManyField(related_name="quiz", to="AdvancedDict.answer"),
        ),
        migrations.AlterField(
            model_name="newword",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 13, 1, 20, 179741)
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="difficulty",
            field=models.IntegerField(
                choices=[(3, "Easy"), (6, "Normal"), (10, "Hard")],
                default=3,
                verbose_name="Difficulty",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 13, 1, 20, 179741)
            ),
        ),
        migrations.DeleteModel(
            name="Question",
        ),
    ]
