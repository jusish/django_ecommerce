from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'is_seller', 'is_buyer']
        
        
    def create(self, validated_data):
        is_seller = validated_data.get('is_seller', False)
        is_buyer = validated_data.get('is_buyer', True) 
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            is_seller=is_seller,
            is_buyer=is_buyer
        )
        user.set_password(validated_data['password'])
        user.save()
        return user;