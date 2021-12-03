from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Poll, Question


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('name', 'start_date', 'end_date', 'description')
        
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        

