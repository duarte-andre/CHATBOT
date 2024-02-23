
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests, json

mockEnabled = True
mockedAnswer = '{"content":"Vai curínthia", "contentId": "383rufu3rhf"}'

psid = "g.a000gAiBy4xcqhGaxE6dzAQ3xxSKl5zZKAAeOlVx6O6gsKr6fF6-8OkpGub-fH23hBr1YezQDgACgYKAToSAQASFQHGX2MiX_B3_EZaEDuN2lY-D2TjfhoVAUF8yKovGSNuca0VUAPHCNzz43-_0076"
psidts = "sidts-CjIBPVxjSnr4FXcutW_MqukpYNed3yJvpFjTH10AM1sjSdRUMYUZIZkKTp5XHLVeDUiOpRAA"
psidcc = "ABTWhQE3tiPfiOdVt3vqPe61QLJJdHdEWXEErIVq4pqv_gFDbDikgoHvVeOWAzNR_3TPX-3cMg"
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

