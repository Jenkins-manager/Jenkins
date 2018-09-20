# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Question
from rest_framework.decorators import api_view
from .serializers import QuestionSerializer
from rest_framework.response import Response
from model.request_processor import RequestProcessor
# Create your views here.
@api_view(['get'])
def get_questions(request):
    questions = Question.objects.all()
    serializer = QuestionSerializer(questions, many=True)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def send_question(request):
    return Response({'body' : {'message': 'hello'}}) if RequestProcessor.check_request(request.data, Question) == True  else Response(status=500, data='Empty Question')
