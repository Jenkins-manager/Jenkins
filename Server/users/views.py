"""
    User controller file
"""
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.decorators import api_view
from rest_framework.response import Response

from model.request_processor import RequestProcessor
from .serializers import UserSerializer
from .models import User

@api_view(['post'])
def send_username(request):
    user_1 = User(username=request.data['body'])
    user_1.save()

@api_view(['get'])
def get_username(_):
    username = User.objects.order_by("-created_at")
    serializer = UserSerializer(username, many=True)
    return Response(serializer.data)
