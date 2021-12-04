from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PollView, QuestionView, SingleQuestionView
from .views import AnswerView, SelectViewSet # , PollListView, PollDetailView


app_name = 'polls'

urlpatterns = [
    # path('', PollListView.as_view(), name='polls'),
    path('polls/', PollView.as_view()),
    # path('<int:pk>/', PollDetailView.as_view(), name='poll'),
    path('polls/<int:pk>/', PollView.as_view()),
    path('questions/', QuestionView.as_view()),
    path('questions/<int:pk>/', SingleQuestionView.as_view()),
    path('answers/', AnswerView.as_view({'get': 'list'})),
    path('answers/<int:pk>/', AnswerView.as_view({'get': 'retrieve'})),
]


router = DefaultRouter()
router.register('selects/', SelectViewSet, basename='user')

urlpatterns += router.urls
