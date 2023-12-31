# Generated by Django 4.2.3 on 2023-08-14 15:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AdvancedDict", "0026_answer_asked_alter_newword_timestamp_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="answer",
            name="question",
            field=models.ManyToManyField(
                related_name="answear", to="AdvancedDict.newword"
            ),
        ),
        migrations.AlterField(
            model_name="newword",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 17, 47, 9, 465286)
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 14, 17, 47, 9, 465286)
            ),
        ),
    ]
