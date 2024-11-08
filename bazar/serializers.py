from rest_framework import serializers
from .models import Product, ProductImage, Sale

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image_url']

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'category', 'price', 'discount_percentage', 'rating', 'stock', 'sku', 'thumbnail', 'tag', 'images']

class SaleSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Sale
        fields = ['id', 'product']
