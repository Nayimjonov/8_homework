from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from .pagination import ProductPagination


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = ProductPagination