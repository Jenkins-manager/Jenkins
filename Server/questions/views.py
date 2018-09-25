# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Question
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from rest_framework.response import Response
from model.request_processor import RequestProcessor
# Create your views here.
@api_view(['get'])
def get_questions(request):
    serializer = RequestProcessor.get_questions(QuestionSerializer, Question)
    return Response(serializer.data)

@api_view(['post'])
def send_question(request):
    request_data = RequestProcessor.check_request(request.data, Question)
    try:
        RequestProcessor.process_request(request_data[1])
        return Response({'message': 'new data', 'data': request.data})
    except:
        return Response(status=500, data='Empty Question')
