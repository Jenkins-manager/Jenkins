# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-17 15:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statement', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('body', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
