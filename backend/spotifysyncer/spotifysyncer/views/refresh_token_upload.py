from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status

from logging import getLogger

from spotifysyncer.serializers.helpers import RefreshTokenUploadSerializer

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

        serialized_request = RefreshTokenUploadSerializer(data=request.data)
        if not serialized_request.is_valid():
            logger.error("Invalid refresh token content")
            return Response(
                serialized_request.errors, status=status.HTTP_400_BAD_REQUEST
            )

        user = request.user
        logger.error(user.id)

        return Response({"user": user.id})
