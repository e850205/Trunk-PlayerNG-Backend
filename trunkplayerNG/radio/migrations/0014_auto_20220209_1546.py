# Generated by Django 3.2.10 on 2022-02-09 23:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0013_auto_20220209_1149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='incident',
            options={'ordering': ['-time']},
        ),
        migrations.AlterField(
            model_name='systemreciverate',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 9, 23, 46, 13, 839842, tzinfo=utc)),
        ),
    ]
