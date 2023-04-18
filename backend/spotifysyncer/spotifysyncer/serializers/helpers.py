from rest_framework import serializers


class CodeToTokenSerializer(serializers.Serializer):
    code = serializers.CharField(
        max_length=256,
        min_length=32,
        allow_blank=False,
        required=True,
        allow_null=False,
    )


class RefreshTokenUploadSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(
        max_length=256,
        min_length=32,
        allow_blank=False,
        required=True,
        allow_null=False,
    )

    expiry = serializers.DateTimeField(required=True)


class RefreshTokenUploadResultSerializer(serializers.Serializer):
    success = serializers.BooleanField(default=False, allow_null=False)
    message = serializers.CharField(
        max_length=128, min_length=4, required=False, allow_null=True
    )
