from django.db import models
from django.shortcuts import render
from rest_framework.generics import get_object_or_404, GenericAPIView, CreateAPIView, ListAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import generics, viewsets


from .models import Poll, Question, Answer, Select
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer, SelectSerializer


class PollView(APIView):
    def get(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response({'polls': serializer.data})

    def post(self, request):
        poll = request.data.get('poll')
        serializer = PollSerializer(data=poll)
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
        return Response({"success": "Poll '{}' created successfully".format(poll_saved.title)})

    def put(self, request, pk):
        saved_poll = get_object_or_404(Poll.objects.all(), pk=pk)
        data = request.data.get('poll')
        serializer = PollSerializer(instance=saved_poll, data=data, partial=True)
        
        if serializer.is_valid(raise_exception=True):
            poll_saved = serializer.save()
            
        return Response({
            "success": "Poll '{}' updated successfully".format(poll_saved.name) 
        })
        
    def delete(self, request, pk):
        poll = get_object_or_404(Poll.objects.all(), pk=pk)
        poll.delete()
        return Response({
            "message": "Poll with id '{}' has been deleted.".format(pk)
        }, status=204)        


class QuestionView(ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    # def get(self, request, *args, **kwargs):
    #     return self.list(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        polls = get_object_or_404(Poll, id=self.request.data.get('polls'))
        return serializer.save(polls=polls)
    
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)


class SingleQuestionView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerView(viewsets.ViewSet):
    """
    A simple ViewSet that for listing or retrieving users.
    """
    def list(self, request):
        queryset = Answer.objects.all()
        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = Answer.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = AnswerSerializer(user)
        return Response(serializer.data)


class SelectViewSet(viewsets.ModelViewSet):
    serializer_class = SelectSerializer
    queryset = Select.objects.all()


# class PollListView(generics.ListAPIView):
#     model = Poll
#     template_name = 'polls/poll_list.html'
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
    

# class PollDetailView(generics.RetrieveAPIView):
#     model = Poll
#     template_name = 'polls/poll_detail.html'
#     queryset = Poll.objects.all()
#     serializer_class = PollSerializer
    