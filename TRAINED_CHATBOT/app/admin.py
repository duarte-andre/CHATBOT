from django.contrib import admin
from .models import *

class adminConversationHistory(admin.ModelAdmin):
    list_display = ('id', 'date', 'user')
    list_display_links = ('id', 'date', 'user')
    search_fields = ('user',)
    list_per_page = 10

admin.site.register(ConversationHistory, adminConversationHistory)

class adminConversation(admin.ModelAdmin):
    list_display = ('id', 'type', 'date', 'history')
    list_display_links = ('id', 'type', 'date', 'history')
    search_fields = ('type','date','history')
    list_per_page = 10

admin.site.register(Conversation, adminConversation)

