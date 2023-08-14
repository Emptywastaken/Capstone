# Generated by Django 4.2.3 on 2023-08-14 11:06

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("AdvancedDict", "0020_alter_quiz_options_remove_answer_question_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="newword",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 13, 6, 21, 220816)
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 13, 6, 21, 220816)
            ),
        ),
    ]