# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class Question(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    body = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=False)

class Answer(models.Model):
    id = models.IntegerField(primary_key=True, null=False)
    body = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=False)