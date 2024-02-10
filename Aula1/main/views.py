
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

psid = ""
psidts = ""
psidcc = ""
#cria um conjunto com os tokens de autenticação
#para poder usar o Bard
tokenCookies = {
    "__Secure-1PSID": psid,
    "__Secure-1PSIDTS": psidts,
    "__Secure-1PSIDCC": psidcc, 
}
#cria o objeto bard para ser usado
bard = BardCookies(cookie_dict=tokenCookies)

#define as ações da API para receber
#os comandos a ser passado para o Bard
class ChatBotAPIView(APIView):
    def post(self, request):
        #pega os dados que veio na requisição
        data = request.data

        print("data received:")
        print(data['question'])

        answer = bard.get_answer(data['question'])

        return Response(status=201,data=answer)

