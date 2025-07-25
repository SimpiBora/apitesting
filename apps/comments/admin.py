from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'text', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', 'user', 'post')
    search_fields = ('user__username', 'post__id', 'text')
