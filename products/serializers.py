from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(source='category')
    category_name = serializers.StringRelatedField(source='category', read_only=True)



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
