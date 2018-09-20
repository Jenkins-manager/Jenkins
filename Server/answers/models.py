# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# from django.contrib.postgres.fields import ArrayField

from django.db import models

# Create your models here.
class Answer(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    answer = models.CharField(max_length=50, null=False)