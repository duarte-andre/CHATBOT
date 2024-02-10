from django.urls import path
from .views import *

urlpatterns = [
    path("chatbot/", ChatBotAPIView.as_view(), name='chatbot')
]
