# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Question
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['get'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)
