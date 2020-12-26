# Generated by Django 3.0.5 on 2020-12-26 01:22

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('replays', '0001_initial'), ('replays', '0002_auto_20201226_0112'), ('replays', '0003_replay_file'), ('replays', '0004_auto_20201226_0119')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Replay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('submitter', models.CharField(max_length=32)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=32, null=True), size=None)),
                ('description', models.TextField(blank=True, null=True)),
                ('event', models.CharField(blank=True, max_length=64, null=True)),
                ('series_count', models.IntegerField(blank=True, null=True)),
                ('downloads', models.IntegerField(default=0)),
                ('map', models.CharField(max_length=32)),
                ('vs', models.CharField(max_length=4)),
                ('type', models.CharField(max_length=32)),
                ('ranked', models.BooleanField()),
                ('game_date', models.DateTimeField(blank=True, null=True)),
                ('mod', models.CharField(blank=True, max_length=32, null=True)),
                ('winner', models.CharField(max_length=4)),
                ('loser', models.CharField(max_length=4)),
                ('winner_domination', models.IntegerField()),
                ('loser_domination', models.IntegerField()),
                ('winner_players', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=32, null=True), size=8)),
                ('loser_players', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=32, null=True), size=8)),
                ('scores', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('replay_name', models.CharField(blank=True, max_length=32, null=True)),
                ('file_name', models.CharField(blank=True, max_length=64, null=True)),
                ('view_side', models.CharField(blank=True, max_length=4, null=True)),
                ('view_player', models.CharField(blank=True, max_length=32, null=True)),
                ('replay_length', models.CharField(blank=True, max_length=5, null=True)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]