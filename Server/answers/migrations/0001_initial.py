# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-20 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('answer', models.CharField(max_length=50)),
            ],
        ),
    ]