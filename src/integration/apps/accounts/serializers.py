from rest_framework import serializers 


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True, max_length=50)
    password = serializers.CharField(required=True, max_length=50)