# Generated by Django 3.2 on 2021-04-22 19:11

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_name', models.TextField()),
                ('species', models.TextField()),
                ('discord_id', models.BigIntegerField()),
                ('color', models.TextField()),
                ('closeness', models.IntegerField()),
                ('size', models.TextField()),
                ('ability_type', models.TextField()),
                ('rarity', models.TextField()),
                ('owner', models.TextField()),
                ('stats', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('eggs', models.IntegerField(default=0)),
                ('discord_id', models.BigIntegerField(default=0)),
                ('coins', models.IntegerField(default=0)),
            ],
        ),
    ]
