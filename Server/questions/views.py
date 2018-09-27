"""
    Questions controller file
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse

from model.request_processor import RequestProcessor
from answers.models import Answer

from .models import Question
from .serializers import QuestionSerializer

@api_view(['get'])
def get_questions(_):
    serializer = RequestProcessor.get_questions(QuestionSerializer, Question)
    return Response(serializer.data)

@api_view(['POST', 'GET'])
def send_question(request):
    request_data = RequestProcessor.check_request(request.data, Question)
    try:
        answer_string = RequestProcessor.process_request(request_data[1], Answer)
    except Exception, e:
        answer_string = RequestProcessor.get_funny_response()
        print(str(e))
    finally:
        print(answer_string)
        return JsonResponse({'answer': answer_string})
