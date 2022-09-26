from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import (
    Category,
    Quiz,
    Question,
    Option
)

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = ''