# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Question
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from rest_framework.response import Response
from Server.model.request_processor import RequestProcessor
# Create your views here.
@api_view(['get'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['post'])
def send_question(request):
    q1 = Question(body=request.data['body'])
    q1.save()
    return Response({'message': 'new data', 'data': request.data}) if RequestProcessor.check_request(request.data, Question) == True  else Response(status=500, data='Empty Question')