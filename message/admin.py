from django.contrib import admin

from message.models import MessageModel


class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'time', 'content']

admin.site.register(MessageModel, MessageAdmin)