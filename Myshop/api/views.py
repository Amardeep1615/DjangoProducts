from django.shortcuts import render,get_object_or_404
from products.models import Product
from .serializers import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins,generics
from rest_framework import viewsets


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
            return Response (serializers.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','PATCH','DELETE'])
def ProdcutDetailAPIView(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    
    elif request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'PATCH':
        serializer = ProductSerializer(product,data=request.data,partial=True)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
        


class Products(APIView):
    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    #Class Baesd Views
class ProductDetail(APIView):
    def get_object(self,id):
        try:
            return Product.objects.get(id = id )
        except:
            Product.DoesNotExist()
            raise Http404


    def get(self,request,id):
        product = self.get_object(id)
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def put(self,request,id):
        product = self.get_object(id)
        serializer = ProductSerializer(product,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,id):
        product = self.get_object(id)
        serializer = ProductSerializer(product,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.erros,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        product = self.get_object(id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Mixins

class ProductsMixin(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)
    

class ProductDetailMixin(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

    def get(self,request,id):
        return self.retrieve(request)
    def put(self,request,id):
        return self.update(request)
    def delete(self,request,id):
        return self.delete(request)    

#Generics 

class ProductsGenericView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductGenericDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

"""
#Viewsets

class ProductsViewset(viewsets.ViewSet):
    lookup_field = 'id'
   
    def list(self,request):
        product = Product.objects.all()
        serializer = ProductSerializer(product,many = True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def create(self,request):
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

    def retrieve(self,request, id = None):
        products = get_object_or_404(Product,id=id)
        serializer = ProductSerializer(products)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def update(self,request, id = None):
        products = get_object_or_404(Product,id = id )
        serializer = ProductSerializer(products)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request, id = None):
        products = get_object_or_404(Product,id = id )
        products.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
"""
       
class ProductsModelViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer







    
    


    
    

    

   