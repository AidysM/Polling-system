from django.db import models
from django.db.models import fields
from rest_framework import serializers

from .models import Poll, Question


class PollSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=256)
    start_date = serializers.DateField()
    end_date = serializers.DateField()
    description = serializers.CharField(max_length=1024)
    
    def create(self, validated_data):
        return Poll.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.end_date = validated_data.get('end_date', instance.end_date)
        instance.description = validated_data.get('description', instance.description)
        
        instance.save()
        return instance
    
    
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'question_type', 'polls', 'options', 'answer_position')
        

