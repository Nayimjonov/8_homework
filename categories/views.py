from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer, CategoryDetailSerializer
from .pagination import CategoryPagination



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CategoryDetailSerializer
        return CategorySerializer
