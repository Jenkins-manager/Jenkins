# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Question(models.Model):
    id = models.IntegerField(null=False)
    body = models.CharField(max_length=50, null=False)
    user_id = models.IntegerField(null=False)
    created_at = models.DateTimeField(null=False)

class Answer(models.Model):
    id = models.IntegerField(null=False)
    body = models.CharField(max_length=50, null=False)
    user_id = models.IntegerField(null=False)
    created_at = models.DateTimeField(null=False)
