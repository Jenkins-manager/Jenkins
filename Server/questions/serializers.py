from rest_framework.serializers import ModelSerializer
from .models import Question

class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__' #can also put in your own fields if you dont want them all
