# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from model.request_processor import RequestProcessor
from .models import User

# Create your views here.

@api_view(['post'])
def send_username(request):
    u1 = User(username=request.data['body'])
    u1.save()
