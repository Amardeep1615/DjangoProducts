from django.shortcuts import render
from products.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','POST'])
def ProductAPIView(request):
    if request.method == 'GET':
       products = Product.objects.all()
       serializers = ProductSerializer(products,many=True)
       return Response(serializers.data,status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializers = ProductSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

