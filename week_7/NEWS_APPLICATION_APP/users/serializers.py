from rest_framework import serializers
from .models import User, Author


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model  = User
        fields = '__all__'  

    def validate(self, attrs):
        return attrs
    
    def create(self, validated_data):
        users = User(
            first_name = validated_data.get('first_name'),
            last_name  = validated_data.get('last_name'),
            email      = validated_data.get('email'),
            role       = validated_data.get('role')
        )

        users.set_password(validated_data.get('password'))
        users.save()
        return users
    


class AuthorSerializer(serializers.ModelSerializer):    
    class Meta:
        model  = Author
        fields = ["user", "biography", "portfolio", "reviews"]
        read_only_fields = ("user")