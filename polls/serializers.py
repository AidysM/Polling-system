from django.db import models
from rest_framework import serializers

from .models import Poll


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('name', 'start_date', 'end_date', 'description')
        
    