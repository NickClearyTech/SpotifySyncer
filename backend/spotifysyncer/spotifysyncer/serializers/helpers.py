from rest_framework import serializers

class CodeToTokenSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=128, min_length=32, allow_blank=False, required=True, allow_null=False)