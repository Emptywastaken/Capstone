# Generated by Django 4.2.3 on 2023-08-12 17:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AdvancedDict", "0014_alter_newword_timestamp_alter_quiz_difficulty_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newword",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 12, 19, 12, 52, 266649)
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="difficulty",
            field=models.IntegerField(
                choices=[("Easy", 3), ("Medium", 6), ("Hard", 10)],
                default="Easy",
                verbose_name="Difficulty",
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 12, 19, 12, 52, 266649)
            ),
        ),
    ]
