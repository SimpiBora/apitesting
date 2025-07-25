from .models import LikesCount
from django.contrib import admin
from .models import Like


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created_at', 'updated_at','post')
    list_filter = ('created_at', 'user', 'post')
    search_fields = ('user__username', 'post__id')

# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'content_summary')
#     search_fields = ('title', 'content')
#     ordering = ('id',)
#     list_per_page = 20

#     def content_summary(self, obj):
#         return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

#     content_summary.short_description = "Content Summary"


@admin.register(LikesCount)
class LikesCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'count', 'usernames_preview', 'post_preview')
    search_fields = ('post__title',)
    ordering = ('-count',)
    list_filter = ('post',)  # Use the direct `post` field for filtering
    list_per_page = 20

    def usernames_preview(self, obj):
        usernames = obj.usernames
        if len(usernames) > 5:
            return ', '.join(usernames[:5]) + "..."
        return ', '.join(usernames)

    def post_preview(self, obj):
        # Access the textual content of the Post object
        post_content = getattr(obj.post, 'post_preview', None)  # Replace 'content' with the actual field name
        if post_content:
            # Return only the first 50 characters of the post content
            return post_content[:50] + "..." if len(post_content) > 50 else post_content
        return "No content available"



    post_preview.short_description = "post"
    usernames_preview.short_description = "Usernames"
