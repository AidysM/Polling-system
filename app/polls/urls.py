from django.urls import path

from .views import PollView, QuestionView, SingleQuestionView
from .views import PollListView, PollDetailView


app_name = 'polls'

urlpatterns = [
    path('', PollListView.as_view(), name='polls'),
    path('polls/', PollView.as_view()),
    path('<int:pk>/', PollDetailView.as_view(), name='poll'),
    path('polls/<int:pk>/', PollView.as_view()),
    path('questions/', QuestionView.as_view()),
    path('questions/<int:pk>/', SingleQuestionView.as_view()),
]
