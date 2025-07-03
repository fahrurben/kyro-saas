from rest_framework import serializers

from core.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, max_length=100, write_only=True)

    class Meta:
        model = CustomUser
        fields = ('id', 'email', 'first_name', 'last_name', 'username', 'password', )