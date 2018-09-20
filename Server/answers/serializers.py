from rest_framework.serializers import ModelSerializer
from .models import Answer

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__' #can also put in your own fields if you dont want them all
