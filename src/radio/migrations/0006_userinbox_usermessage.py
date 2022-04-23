# Generated by Django 3.2.10 on 2022-04-23 15:22

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0005_transmission_audio_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('urgent', models.BooleanField(default=False)),
                ('read', models.BooleanField(default=False)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('source', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserInbox',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('messages', models.ManyToManyField(to='radio.UserMessage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.userprofile')),
            ],
        ),
    ]
