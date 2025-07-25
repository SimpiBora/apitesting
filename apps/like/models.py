from django.core.cache import cache
from django.db import models
# from accounts.models import Post, AutoUpdate, User

from apps.postsapi.models import Post

# from accounts.models import AutoUpdate, User
from apps.core.models import AutoUpdate
from django.contrib.auth import get_user_model

User = get_user_model()


class LikeManager(models.Manager):
    def likes_count_for_post(self, post_id):
        return self.filter(post_id=post_id).count()


class Like(AutoUpdate):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="liked_user")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post")

    objects = LikeManager()

    def __str__(self):
        return f"Like by {self.user.username} on Post {self.post.id} and { self.post.text[:20] }..."


class LikesCount(models.Model): 
    post = models.OneToOneField(
        Post, on_delete=models.CASCADE, related_name="likes_count"
    )
    count = models.PositiveIntegerField(default=0)
    # Stores usernames of users who liked
    usernames = models.JSONField(default=list)

    CACHE_TIMEOUT = 300  # Cache timeout in seconds (e.g., 5 minutes)

    @staticmethod
    def get_cache_key(post_id):
        return f"post_{post_id}_likes_count"

    @classmethod
    def get_cached_likes_count(cls, post_id):
        cache_key = cls.get_cache_key(post_id)
        count = cache.get(cache_key)

        if count is None:
            try:
                likes_count = cls.objects.get(post_id=post_id)
                count = likes_count.count
                cache.set(cache_key, count, timeout=cls.CACHE_TIMEOUT)
            except cls.DoesNotExist:
                count = 0
                cache.set(cache_key, count, timeout=cls.CACHE_TIMEOUT)

        return count

    @classmethod
    def invalidate_cache(cls, post_id):
        cache_key = cls.get_cache_key(post_id)
        cache.delete(cache_key)

    def add_like(self, username):
        if username not in self.usernames:
            self.usernames.append(username)
            self.count += 1
            self.save()
            # Invalidate cache after update
            self.invalidate_cache(self.post.id)

    def remove_like(self, username):
        if username in self.usernames:
            self.usernames.remove(username)
            self.count -= 1
            self.save()
            # Invalidate cache after update
            self.invalidate_cache(self.post.id)

    def __str__(self):
        return f"Post {self.post.id} has {self.count}[:10] likes"
