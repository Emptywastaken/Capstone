# Generated by Django 4.2.3 on 2023-08-10 16:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("AdvancedDict", "0006_remove_newword_source_language_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="newword",
            name="timestamp",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 8, 10, 18, 12, 44, 848287)
            ),
        ),
    ]
