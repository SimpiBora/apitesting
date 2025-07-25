from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Comment
from rest_framework.response import Response
from rest_framework import status
from .serializers import CommentSerializer

from rest_framework.viewsets import ViewSet
from rest_framework.authentication import SessionAuthentication
from drf_spectacular.utils import extend_schema

# views.py
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Comment, Post
from .serializers import CommentSerializer
from rest_framework.decorators import action
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Comment
from .serializers import CommentSerializer


class CommentsViewSet(ViewSet):
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=None,
        parameters=[
            OpenApiParameter(name="post_id", required=True, type=int, location="query"),
            OpenApiParameter(name="comment", required=True, type=str, location="query"),
        ],
        responses={201: CommentSerializer},
        tags=["Comments"],
    )
    @action(detail=False, methods=["post"])
    def post(self, request):
        """
        API to create a comment on a post.
        Expects: { "post_id": int, "comment": str }
        Returns: created comment and success message.
        """
        post_id = request.data.get("post_id")
        comment_text = request.data.get("comment")

        if not post_id or not comment_text:
            return Response(
                {"error": "Both post_id and comment are required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return Response(
                {"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND
            )

        try:
            comment = Comment.objects.create(
                post=post,
                user=request.user,
                text=comment_text,
            )

            return Response(
                {
                    "comment": CommentSerializer(
                        comment, context={"request": request}
                    ).data,
                    "success": "OK",
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class CommentDeleteViewSet(ViewSet):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    @extend_schema(
        request=None,
        parameters=[
            OpenApiParameter(name="post_id", required=True, type=int, location="query"),
            OpenApiParameter(name="comment", required=True, type=str, location="query"),
        ],
        responses={201: CommentSerializer},
        tags=["Comments"],
    )

    def destroy(self, request, pk=None):
        # Retrieve the comment or return 404
        comment = get_object_or_404(Comment, pk=pk)
        # Enforce object-level permission
        self.check_object_permissions(request, comment)

        if request.user != comment.user:
            return Response(
                {"error": "Permission denied"},
                status=status.HTTP_403_FORBIDDEN
            )

        # Serialize the comment before deletion (optional)
        serializer = CommentSerializer(comment)

        comment.delete()
        return Response(
            {"comment": serializer.data, "success": "OK"},
            status=status.HTTP_200_OK
        )
