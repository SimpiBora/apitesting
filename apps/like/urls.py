# from rest_framework.routers import DefaultRouter
# from django.urls import path, include

# router = DefaultRouter()
# # router.register(r'posts', PostViewSet, basename='post')

# # Combine the manual URLs and router-generated URLs
# # urlpatterns += router.urls


# # Define your URL patterns
# urlpatterns = [
#     path('', include('route.urls'))
# ]

from inspect import getmembers, isclass

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.viewsets import ViewSet

from . import views

router = DefaultRouter()

# Automatically find all ViewSets in views.py and register them
for name, cls in getmembers(views, isclass):
    if issubclass(cls, ViewSet) and cls.__module__ == views.__name__:
        router.register(
            rf"{name.lower().replace('viewset', '')}", cls, basename=name.lower()
        )

# router.register(r"productlist", views.ProductListViewSet, basename="productlist")

urlpatterns = [
    # Register the routes under '/api/mod5/'
    path("", include(router.urls)),
    # Manually add the custom path for DynamicCategoryURLFilterViewSet
]

# from django.urls import path
# from .views import LikeCreateView, LikeDeleteView, LikeView
# # from .views import LikesCountView, LikeCreateView, LikeDeleteView, LikeView

# urlpatterns = [
#     # path('posts/<int:post_id>/likes-count/',
#     #      LikesCountView.as_view(), name='likes-count'),
#     path('likes', LikeView.as_view(), name='like-list'),
#     path('likes/create/', LikeCreateView.as_view(), name='like_create'),
#     path('likes/<int:id>/delete/', LikeDeleteView.as_view(), name='like_delete'),
# ]
