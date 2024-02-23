from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','email','is_superuser','first_name','last_login')
        many = True

class ConversationHistorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = ConversationHistory
        fields = '__all__'
        many = True

class ConversationSerializer(serializers.ModelSerializer):
    history = ConversationHistorySerializer(read_only=True)
    class Meta:
        model = Conversation
        fields = '__all__'
        many = True

