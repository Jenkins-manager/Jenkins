"""
    Serializer for answers
"""

from rest_framework.serializers import ModelSerializer
from .models import Answer

class AnswerSerializer(ModelSerializer):

    def __init__(self):
        pass
        
    class Meta:
        model = Answer
        fields = '__all__' #can also put in your own fields if you dont want them all
