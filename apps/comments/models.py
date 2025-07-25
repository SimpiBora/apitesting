from django.db import models

# from accounts.models import User, Post, AutoUpdate
from apps.core.models import AutoUpdate
from django.contrib.auth import get_user_model
from apps.postsapi.models import Post

User = get_user_model()


# class Comment(AutoUpdate):
#     user = models.ForeignKey(
#         User,
#         on_delete=models.CASCADE,
#         related_name='comments'
#     )
#     post = models.ForeignKey(
#         Post,
#         on_delete=models.CASCADE,
#         related_name='comments'
#     )
#     text = models.TextField()
#     # created_at = models.DateTimeField(auto_now_add=True)
#     # updated_at = models.DateTimeField(auto_now=True)

#     def __str__(self):
#         return f"Comment by {self.user.username} on Post {self.post.id}"
# from django.db import models
from django.core.exceptions import ValidationError


class Comment(AutoUpdate):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.username} on Post {self.post.id}: {self.text[:20]}..."

    def clean(self):
        if not self.text.strip():
            raise ValidationError("Comment text cannot be empty.")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
        indexes = [
            models.Index(fields=["post"]),
            models.Index(fields=["user"]),
        ]
