from django.db import models
from django.contrib.auth.models import User

CONVERSATION_TYPE = [
    ("Q", "Question"),
    ("A", "Answer")
]

class ConversationHistory(models.Model):   
    date = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class Conversation(models.Model):
    type = models.CharField(max_length=100, choices=CONVERSATION_TYPE)
    message = models.CharField(max_length=3000)
    date = models.DateField(auto_now_add=True)
    history = models.ForeignKey(ConversationHistory, related_name='history', on_delete=models.CASCADE)

    def __str__(self):
        return self.message