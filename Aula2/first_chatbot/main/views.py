
from rest_framework.views import APIView
from rest_framework.response import Response
from bardapi import BardCookies
import requests

psid = "g.a000gAikfuDWYsLay0sLjWQ1ZHExOEET68My8jxveoQIiL9Mal5GvafvYK0u9Eg4LZMAN1GdgQACgYKAXASAQASFQHGX2Mi8gKKK5bW9qOHAD46jIqqqxoVAUF8yKrHsCWJQNE7a9uElcTe3Ds70076"
psidts = "sidts-CjEBPVxjShR72qmZvzmOjROVUtUpiJxOYEHSFom9dfM0xwMpkEnUghwH5_3jpvV_7YJBEAA"
psidcc = "ABTWhQGN-NsVDAVTdpUeWIWYv98pofPC3HaPht-rWpJsA8JPOK2gRxW-RHHt0jGI-QiCUWwc9Yc"
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

