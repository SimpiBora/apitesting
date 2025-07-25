from .models import Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'text', 'user','post']

    def get_user(self, obj):
        request = self.context.get("request")
        user = obj.user

        print(f"[DEBUG] Entered get_user for user ID: {getattr(user, 'id', 'Unknown')}")
        print(
            f"[DEBUG] Has image attribute? {'Yes' if hasattr(user, 'image') else 'No'}"
        )

        image_url = None
        if hasattr(user, "image") and user.image and hasattr(user.image, "url"):
            print(f"[DEBUG] Image field exists and is set: {user.image}")
            try:
                raw_url = user.image.url
                print(f"[DEBUG] Raw image URL: {raw_url}")
                image_url = (
                    request.build_absolute_uri(raw_url)
                    if request
                    else f"{settings.MEDIA_URL}{raw_url}"
                )
                print(f"[DEBUG] Final image URL: {image_url}")
            except ValueError as e:
                print(f"[ERROR] No image file associated with user {user.id}: {e}")
            except Exception as e:
                print(
                    f"[ERROR] Unexpected error while resolving image URL for user {user.id}: {e}"
                )
        else:
            print(f"[WARNING] User {user.id} has no image or it's empty.")

        return {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "image": image_url,
        }
