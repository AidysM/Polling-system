from django.urls import path

from .views import PollListView


app_name = 'polls'

urlpatterns = [
    path('', PollListView.as_view(), name='polls'),
    
]
