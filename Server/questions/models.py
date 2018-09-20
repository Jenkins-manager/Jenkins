# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

# Create your models here.
class Question(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    body = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=False)
    address = models.IntegerField(null=False, default=0)
