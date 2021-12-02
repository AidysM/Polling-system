from django.db import models
from django.shortcuts import render
from django.views.generic import ListView

from .models import Poll, Question


class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'
    

