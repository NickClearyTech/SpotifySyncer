from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response

from logging import getLogger

logger = getLogger(__name__)


class CallbackEndpoint(APIView):
    """
    View to handle the /callback url
    """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        logger.error(self.request.query_params.get("code"))

        return Response({"hello": "there"})
