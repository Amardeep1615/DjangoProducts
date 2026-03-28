from django.contrib import admin
from products.models import Product

# Register your models here.
@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_id','product_name','product_desc','product_stock']
    list_filter = ['product_name','product_desc','product_stock']
    search_fields = ['product_name','product_desc','product_stock']
    list_per_page = 10


