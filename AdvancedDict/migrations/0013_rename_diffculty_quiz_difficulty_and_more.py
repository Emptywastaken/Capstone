# Generated by Django 4.2.3 on 2023-08-12 17:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AdvancedDict", "0012_rename_diffcutly_quiz_diffculty_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="quiz",
            old_name="diffculty",
            new_name="difficulty",
        ),
        migrations.AlterField(
            model_name="newword",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 12, 19, 2, 56, 275770)
            ),
        ),
        migrations.AlterField(
            model_name="quiz",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 12, 19, 2, 56, 275770)
            ),
        ),
    ]