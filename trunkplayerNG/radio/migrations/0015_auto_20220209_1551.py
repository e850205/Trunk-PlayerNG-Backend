# Generated by Django 3.2.10 on 2022-02-09 23:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0014_auto_20220209_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='systemreciverate',
            name='recorder',
        ),
        migrations.DeleteModel(
            name='Call',
        ),
        migrations.DeleteModel(
            name='SystemReciveRate',
        ),
    ]
