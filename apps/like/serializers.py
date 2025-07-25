from .models import Like
from rest_framework import serializers


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id', 'user_id', 'post_id']
