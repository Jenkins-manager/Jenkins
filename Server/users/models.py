"""
    Question model definition
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True, null=False, unique=True)
    username = models.CharField(max_length=50, null=False)
    created_at = models.DateTimeField(default=datetime.now, blank=True, null=False)
