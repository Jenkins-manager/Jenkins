"""
    Questions controller file
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from Jenkins.Server.model.request_processor import RequestProcessor
from .models import Question
from .serializers import QuestionSerializer

@api_view(['get'])
def get_questions(_):
    serializer = RequestProcessor.get_questions(QuestionSerializer, Question)
    return Response(serializer.data)

@api_view(['post'])
def send_question(request):
    request_data = RequestProcessor.check_request(request.data, Question)
    try:
        RequestProcessor.process_request(request_data[1])
        return Response({'message': 'new data', 'data': request.data})
    except Exception, e:
        return Response(status=500, data='Empty Question')
