from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    Category,
    Quiz,
    Question,
    Option
)
from .serializers import (
    CategorySerializer,
    QuizSerializer
)


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class QuizList(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['category']
