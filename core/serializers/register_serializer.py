from rest_framework import serializers
from ..models import CustomUser, Company
from ..services.user_service import register_new_user

class RegisterSerializer(serializers.Serializer):
    company_name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, min_length=6)

    def validate_company_name(self, value):
        is_exists = Company.objects.filter(name__iexact=value).exists()
        if is_exists:
            raise serializers.ValidationError("Company name already registered")
        return value

    def validate_email(self, value):
        is_exists = CustomUser.objects.filter(email__iexact=value).exists()
        if is_exists:
            raise serializers.ValidationError("Email already registered")
        return value

    def create(self, validated_data):
        user = register_new_user(**validated_data)
        return user