
from rest_framework import generics
from .models import (
    Category,
    Quiz,
    Question,
    Option
)
from .serializers import CategorySerializer

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ''