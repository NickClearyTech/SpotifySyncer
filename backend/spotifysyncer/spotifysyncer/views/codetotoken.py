from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from rest_framework import status

from spotifysyncer.serializers.helpers import CodeToTokenSerializer

from logging import getLogger

logger = getLogger(__name__)

class CodeToToken(APIView):
    """
    View to handle the /codetotoken url
    """

    permission_classes = [permissions.AllowAny]

    def post(self, request, format=None):
        if request.content_type != "application/json":
            logger.error("Invalid content type")
            return Response({"Invalid Content Type", "Use application/json"}, status=status.HTTP_415_UNSUPPORTED_MEDIA_TYPE)

        return Response({"hello": "there"})