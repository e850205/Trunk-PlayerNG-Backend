# Generated by Django 3.2.10 on 2022-01-03 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("radio", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="systemreciverate",
            name="time",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 1, 3, 15, 45, 5, 564247)
            ),
        ),
    ]
