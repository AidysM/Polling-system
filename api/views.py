from rest_framework import generics

from polls.models import Poll
from .serializers import PollSerializer


class PollAPIView(generics.ListAPIView):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    