
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests, json

mockEnabled = False
mockedAnswer = '{"content":"Vai curínthia", "contentId": "383rufu3rhf"}'

psid = "g.a000ggiBy7SSARymNkGQU5KhuWLjEdD0srtAkNKH-mLo_3qSMjdwuFe00GfC2OV_XHqu15hSngACgYKAbYSAQASFQHGX2MiyiXF6NDJElAkok2QSoscuBoVAUF8yKot61BX9gIJdMaAPZcG5xY-0076"
psidts = ""
psidcc = "ABTWhQEI7XotPyGJJy4q6OrSbFpcaR9PLABgzBEjYPQaOpKAxPAJ2L4sYA9mnk6qYYHWOw05Aw"
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}


#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        if mockEnabled == True:            
            return Response(status=201,data=json.loads(mockedAnswer))

        #cria o objeto bard para ser usado
        bard = BardCookies(cookie_dict=tokenCookies)

        #pega os dados que veio na requisição
        data = request.data

        #pega o dados da conversationId caso ele seja informado para mander a mesma conversa com o chatbot
        conversationId = data.get("conversationId")

        #verifica se o id da conversa foi recebido
        if(conversationId is not None):

            #informa o bard para responder na conversa desejada
            bard.conversation_id = conversationId
        else:
            bard.conversation_id = None
        
        answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

