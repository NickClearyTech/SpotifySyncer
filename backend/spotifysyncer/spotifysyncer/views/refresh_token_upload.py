from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from logging import getLogger

from spotifysyncer.serializers.helpers import RefreshTokenUploadSerializer
from spotifysyncer.utils.encryption import encrypt, decrypt
from spotifysyncer.models import SpotifyKey

logger = getLogger(__name__)


class RefreshTokenUpload(APIView):
    """
    View to handle the uploading of a spotify refresh token
    """

    def post(self, request, format=None):
        if request.content_type != "application/json":
            logger.error("Invalid content type")
            return Response(
                {"Invalid Content Type", "Use application/json"},
                status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE,
            )

        user = request.user

        serialized_request: RefreshTokenUploadSerializer = RefreshTokenUploadSerializer(
            data=request.data
        )
        if not serialized_request.is_valid():
            logger.error(f"Invalid refresh token content for user with ID {user}")
            return Response(
                serialized_request.errors, status=status.HTTP_400_BAD_REQUEST
            )

        encrypted_token: bytes = encrypt(serialized_request.data["refresh_token"])

        token_object: SpotifyKey = SpotifyKey.objects.filter(user=user).first()

        if token_object is None:
            token_object = SpotifyKey()
            token_object.user = user

        logger.error(token_object)
        token_object.refresh_key = encrypted_token
        token_object.expires = serialized_request.data["expiry"]

        token_object.save()

        logger.info(
            f"Successfully uploaded refresh token for user with ID {user.id} with expiration time of {serialized_request.data['expiry']}"
        )

        return Response({"user": user.id, "saved": True})
