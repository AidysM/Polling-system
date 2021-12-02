from django.urls import path

from .views import PollAPIView


app_name = 'api'

urlpatterns = [
    path('', PollAPIView.as_view()),
]
