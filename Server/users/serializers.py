"""
    User Serializer file
"""

from rest_framework.serializers import ModelSerializer
from .models import User

class UserSerializer(ModelSerializer):

    def __init__(self):
        pass

    class Meta:
        model = User
        fields = '__all__'
