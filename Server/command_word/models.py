# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.

class CommandWord(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    word = models.CharField(max_length=30, null=False, default='none')
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=False)
    word_action = models.CharField(max_length=50, null=True)