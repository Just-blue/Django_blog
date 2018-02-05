from django.contrib import admin

from comments.models import CommentModel


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'created_time', 'post', 'text']

admin.site.register(CommentModel, CommentAdmin)