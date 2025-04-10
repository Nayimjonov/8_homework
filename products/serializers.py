from rest_framework import serializers
from .models import Product
from categories.models import Category


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category', queryset=Category.objects.all())
    category_name = serializers.StringRelatedField(source='category', read_only=True)
    category_by_name = serializers.CharField(source='category.name', read_only=True)
    images = serializers.JSONField(required=False)

    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'price',
            'discount_price',
            'category_id',
            'category_name',
            'category_by_name',
            'images',
            'stock',
            'is_active',
            'created_at',
            'updated_at',
        )

    def create(self, validated_data):
        images = validated_data.pop('images', [])
        product = Product.objects.create(**validated_data)
        product.images.set(images)
        return product


