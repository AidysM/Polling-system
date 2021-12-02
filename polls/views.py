from django.db import models
from django.shortcuts import render
from rest_framework import generics


from .models import Poll, Question
from .serializers import PollSerializer


class PollListView(generics.ListAPIView):
    model = Poll
    template_name = 'polls/poll_list.html'
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    

class PollDetailView(generics.RetrieveAPIView):
    model = Poll
    template_name = 'polls/poll_detail.html'
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    