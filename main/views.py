from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product
from main.serializers import ProductSerializer


class HelloWorldView(APIView):
    def get(self, request):
        return Response('Hello WORLD!')


class CreateProductView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
