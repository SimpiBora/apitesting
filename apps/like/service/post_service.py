from postsapi.models import Post
from django.db.models import Count


class PostService:
    @staticmethod
    def get_likes_count(post):
        return post.likes.count()

    # @staticmethod
    # def get_top_liked_posts(limit=10):
    #     return Post.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')[:limit]
