from rest_framework import serializers
from .models import Category


class ProductCategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(read_only=True)
    price = serializers.DecimalField(read_only=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id',
            'name',
            'description',
            'parent',
            'image',
            'created_at',
            'updated_at'
        ]

class CategoryDetailSerializer(CategorySerializer):
    parent_name = serializers.SerializerMethodField()
    products_info = serializers.SerializerMethodField()

    class Meta(CategorySerializer.Meta):
        fields = super().fields + ['parens_name', 'products_info']

    def get_parent_name(self, instance):
        return instance.parent_name

    def get_product_info(self, instance):
        return {
            'count': instance.products.count(),
            'products': ProductCategorySerializer(instance.products).data
        }

# class CategoryDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(read_only=True)
#     description = serializers.CharField(read_only=True)
#     parent = serializers.IntegerField(read_only=True)
#     parent_name = serializers.SerializerMethodField()
#     image = serializers.ImageField(read_only=True)
#     products_info = serializers.SerializerMethodField()
#     created_at = serializers.DateTimeField(read_only=True)
#     updated_at = serializers.DateTimeField(read_only=True)
#
#     def get_parent_name(self, obj):
#         return obj.parent_name
#
#     def get_product_info(self, obj):
#         return {
#             'count': obj.products.count(),
#             'products': ProductCategorySerializer(obj.products).data
#         }
