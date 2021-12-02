from django.urls import path

from .views import PollListView, PollDetailView


app_name = 'polls'

urlpatterns = [
    path('', PollListView.as_view(), name='polls'),
    path('<int:pk>/', PollDetailView.as_view(), name='poll'),
    
]
