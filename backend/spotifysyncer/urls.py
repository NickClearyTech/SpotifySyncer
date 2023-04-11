# URL Configuration

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from spotifysyncer.views.callback import CallbackEndpoint
from spotifysyncer.views.codetotoken import CodeToToken
from spotifysyncer.views.refresh_token_upload import RefreshTokenUpload


router = routers.SimpleRouter()
urlpatterns = [
    path("api/v1/", include(router.urls)),
    path("api/v1/schema", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/docs",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("admin/", admin.site.urls),
    re_path(r"api/v1/auth/", include("drf_social_oauth2.urls", namespace="drf")),
    path("api/v1/callback/", CallbackEndpoint.as_view()),
    path("api/v1/codetotoken/", CodeToToken.as_view()),
    path("api/v1/refreshtoken/", RefreshTokenUpload.as_view()),
]
