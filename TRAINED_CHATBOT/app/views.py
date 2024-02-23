from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

from ai import train, chat

from django.http import JsonResponse


class ChatBotAPIView(APIView):
    def get(self, request, conversationId=''):
        chatFound = None

        if conversationId == '':
            chatFound = Conversation.objects.filter(history__id=conversationId)            
        elif 'userId' in request.GET:
            chatFound = Conversation.objects.filter(history__user__id=request.GET['userId'])           
        else:
            chatFound = Conversation.objects.all()
            
        chatFoundSerialized = ConversationSerializer(chatFound, many=True)
        return Response(chatFoundSerialized.data)


    def post(self, request):
        data = request.data

        question = data.get('question')
        conversationId = data.get('conversationId')
        

        answer = chat.get_response(question)
        
        return JsonResponse(status=201, data={'message': answer})