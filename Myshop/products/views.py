from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from products.models import Product
# Create your views here.

def home(request):
    homeurl=f'''
            <h1>Hello Products<h1>
            <p>Cart please!</p>
            '''
    return HttpResponse(homeurl)

def index(request):
    products = Product.objects.all()
    products_list = list(products.values())
    return JsonResponse(products_list,safe=False)

