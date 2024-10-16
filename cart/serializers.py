from rest_framework import serializers
from .models import CartItem
from products.serializers import ProductSerializer
from users.models import User
from products.models import Product



class CartItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, source='product')
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    
    class Meta:
        model = CartItem
        fields = ['id', 'product_id', 'quantity', 'user']