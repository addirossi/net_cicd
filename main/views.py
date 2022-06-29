from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView

from main.models import Product
from main.serializers import ProductSerializer


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
