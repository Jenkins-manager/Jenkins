"""
    answer module controller
"""

# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from .models import Answer
from .serializers import AnswerSerializer
from rest_framework.response import Response

# Create your views here.
@api_view(['get'])
def get_answer(_):
    answers = Answer.objects.all()
    serializer = AnswerSerializer(answers, many=True)
    return Response(serializer.data)
