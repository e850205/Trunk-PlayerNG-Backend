# Generated by Django 3.2.8 on 2021-11-02 02:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0004_alter_systemreciverate_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='systemreciverate',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 2, 2, 44, 52, 613949)),
        ),
    ]
