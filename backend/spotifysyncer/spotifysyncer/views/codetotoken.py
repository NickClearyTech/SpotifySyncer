from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status

import requests
import base64

from settings import (
    SOCIAL_AUTH_SPOTIFY_KEY,
    SOCIAL_AUTH_SPOTIFY_SECRET,
    SPOTIFY_REDIRECT_URI,
)

from spotifysyncer.serializers.helpers import CodeToTokenSerializer

from logging import getLogger

logger = getLogger(__name__)


class CodeToToken(APIView):
    """
    View to handle the /codetotoken url
    This allows for the Spotify Developer Client Secret to remain secret.
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        if request.content_type != "application/json":
            logger.error("Invalid content type")
            return Response(
                {"Invalid Content Type", "Use application/json"},
                status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            )

        serialized_request = CodeToTokenSerializer(data=request.data)
        if not serialized_request.is_valid():
            logger.error("Invalid Code To Token content")
            return Response(
                serialized_request.errors, status=status.HTTP_400_BAD_REQUEST
            )

        r = requests.post(
            "https://accounts.spotify.com/api/token",
            data={
                "code": serialized_request.data["code"],
                "grant_type": "authorization_code",
                "redirect_uri": SPOTIFY_REDIRECT_URI,
            },
            headers={
                "Authorization": f"Basic {base64.b64encode(f'{SOCIAL_AUTH_SPOTIFY_KEY}:{SOCIAL_AUTH_SPOTIFY_SECRET}'.encode('ascii')).decode('ascii')}"
            },
        )

        if not r.ok:
            logger.error(f"Error response converting spotify code to token: {r.json()}")
            try:
                return Reponse(r.json(), status=status.HTTP_400_BAD_REQUEST)
            except:
                return Response({"Error": "Error getting response from Spotify API"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(r.json())
