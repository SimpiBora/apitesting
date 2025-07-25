"""
URL configuration for apitesting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# DRF Spectacular imports
from drf_spectacular.views import (
    SpectacularAPIView,
    # SpectacularRedocView,
    SpectacularSwaggerView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    # API apps
    # path("api/", include("api.urls")),
    path("api/", include("apps.accounts.urls")),
    path("api/", include("apps.like.urls")),
    path("api/", include("apps.comments.urls")),
    path("api/", include("apps.search.urls")),
    path("api/", include("apps.postsapi.urls")),
    # DRF Spectacular schema and docs
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    # path(
    #     "api/docs/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    # ),
]

# Static & Media file serving in debug
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
