
from django.core.cache import cache
from .models import Like


class LikeCache:
    CACHE_TIMEOUT = 300  # Cache timeout in seconds (5 minutes)

    @staticmethod
    def get_cache_key(post_id):
        """
        Generates a unique cache key for likes count of a post.
        """
        return f'post_{post_id}_likes_count'

    @staticmethod
    def get_cached_likes_count(post_id):
        """
        Retrieves the cached likes count for the given post.
        """
        cache_key = LikeCache.get_cache_key(post_id)
        count = cache.get(cache_key)

        if count is None:
            # Cache miss, fetch from database
            count = Like.objects.filter(post_id=post_id).count()
            cache.set(cache_key, count, timeout=LikeCache.CACHE_TIMEOUT)

        return count

    @staticmethod
    def update_likes_cache(post_id):
        """
        Updates the cache with the latest likes count for the given post.
        """
        count = Like.objects.filter(post_id=post_id).count()
        cache.set(LikeCache.get_cache_key(post_id),
                  count, timeout=LikeCache.CACHE_TIMEOUT)

    @staticmethod
    def invalidate_cache(post_id):
        """
        Invalidates the cache for the given post.
        """
        cache_key = LikeCache.get_cache_key(post_id)
        cache.delete(cache_key)
