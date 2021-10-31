# Generated by Django 3.2.8 on 2021-10-30 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Call',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('trunkRecorderID', models.CharField(max_length=30)),
                ('startTime', models.DateTimeField(db_index=True)),
                ('endTime', models.DateTimeField(blank=True, null=True)),
                ('active', models.BooleanField(default=True)),
                ('emergency', models.BooleanField(default=True)),
                ('encrypted', models.BooleanField(default=True)),
                ('frequency', models.FloatField()),
                ('phase2', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GlobalAnnouncement',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('enabled', models.BooleanField(default=False)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='GlobalEmailTemplate',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('type', models.CharField(choices=[('welcome', 'welcome'), ('alert', 'alert')], max_length=30, unique=True)),
                ('enabled', models.BooleanField(default=False)),
                ('HTML', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemForwarder',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('feedKey', models.UUIDField(default=uuid.uuid4, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SystemReciveRate',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('time', models.DateTimeField(default=datetime.datetime(2021, 10, 30, 15, 59, 58, 284524))),
                ('rate', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SystemRecorder',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('siteID', models.CharField(blank=True, max_length=100, null=True)),
                ('enabled', models.BooleanField(default=False)),
                ('forwarderWebhookUUID', models.UUIDField(default=uuid.uuid4)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
            ],
        ),
        migrations.CreateModel(
            name='TalkGroup',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('decimalID', models.IntegerField(db_index=True)),
                ('alphaTag', models.CharField(max_length=30)),
                ('commonName', models.CharField(blank=True, max_length=10, null=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('encrypted', models.BooleanField(default=True)),
                ('agency', models.ManyToManyField(null=True, to='radio.Agency')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('siteAdmin', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
                ('siteTheme', models.TextField(blank=True, null=True)),
                ('feedAllowed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('decimalID', models.IntegerField(db_index=True)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
            ],
        ),
        migrations.CreateModel(
            name='TransmissionUnit',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('time', models.DateTimeField(db_index=True)),
                ('pos', models.IntegerField(default=0)),
                ('emergency', models.IntegerField(default=0)),
                ('signal_system', models.IntegerField(default=0)),
                ('tag', models.IntegerField(default=0)),
                ('length', models.FloatField(default=0.0)),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.unit')),
            ],
        ),
        migrations.CreateModel(
            name='Transmission',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('startTime', models.DateTimeField(db_index=True)),
                ('endTime', models.DateTimeField(blank=True, null=True)),
                ('audioFile', models.FileField(upload_to='')),
                ('encrypted', models.BooleanField(default=False)),
                ('frequency', models.FloatField(default=0.0)),
                ('length', models.FloatField(default=0.0)),
                ('recorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.systemrecorder')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
                ('talkgroup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.talkgroup')),
                ('units', models.ManyToManyField(to='radio.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='TalkGroupACL',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('defualtNewUsers', models.BooleanField(default=True)),
                ('defualtNewTalkgroups', models.BooleanField(default=True)),
                ('allowedTalkgroups', models.ManyToManyField(to='radio.TalkGroup')),
                ('users', models.ManyToManyField(to='radio.UserProfile')),
            ],
        ),
        migrations.CreateModel(
            name='SystemRecorderMetrics',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('calls', models.ManyToManyField(to='radio.Call')),
                ('rates', models.ManyToManyField(to='radio.SystemReciveRate')),
                ('systemRecorder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
            ],
        ),
        migrations.AddField(
            model_name='systemrecorder',
            name='talkgroupsAllowed',
            field=models.ManyToManyField(blank=True, related_name='SRTGAllow', to='radio.TalkGroup'),
        ),
        migrations.AddField(
            model_name='systemrecorder',
            name='talkgroupsDenyed',
            field=models.ManyToManyField(blank=True, related_name='SRTGDeny', to='radio.TalkGroup'),
        ),
        migrations.AddField(
            model_name='systemrecorder',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.userprofile'),
        ),
        migrations.CreateModel(
            name='SystemACL',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_index=True, max_length=100, unique=True)),
                ('public', models.BooleanField(default=False)),
                ('users', models.ManyToManyField(to='radio.UserProfile')),
            ],
        ),
        migrations.AddField(
            model_name='system',
            name='systemACL',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.systemacl'),
        ),
        migrations.CreateModel(
            name='ScanList',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('public', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.userprofile')),
                ('talkgroups', models.ManyToManyField(to='radio.TalkGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('agency', models.ManyToManyField(to='radio.Agency')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.system')),
                ('transmission', models.ManyToManyField(to='radio.Transmission')),
            ],
        ),
        migrations.CreateModel(
            name='GlobalScanList',
            fields=[
                ('UUID', models.UUIDField(db_index=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=30)),
                ('enabled', models.BooleanField(default=False)),
                ('scanList', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.scanlist')),
            ],
        ),
        migrations.AddField(
            model_name='call',
            name='talkgroup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.talkgroup'),
        ),
        migrations.AddField(
            model_name='call',
            name='units',
            field=models.ManyToManyField(to='radio.Unit'),
        ),
        migrations.AddField(
            model_name='agency',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.city'),
        ),
    ]
