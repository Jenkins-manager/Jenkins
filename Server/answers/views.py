"""
    answer module controller
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Answer
from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import AnswerSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['get'])
def get_answer(request):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)
