from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """Serializes our testing for Hello APIView"""
    name = serializers.CharField(max_length=10)

