
from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('products',views.ProductsModelViewset,basename='product')


urlpatterns = [

    #Funtion Based Views(FBV)
    path('apis/',views.ProductAPIView),
    path('api/<int:id>/',views.ProdcutDetailAPIView),
    
    #Class Based Views(CBV)
    path('products/',views.Products.as_view()),
    path('product/<int:id>/',views.ProductDetail.as_view()),

    # Mixins
    path('productsmn/',views.ProductsMixin.as_view()),
    path('productmn/<int:id>/',views.ProductDetailMixin.as_view()),

    #Generics
    path('productsgn/',views.ProductsGenericView.as_view()),
    path('productgn/<int:id>/',views.ProductGenericDetailView.as_view()),

    #ViewSets

    path('',include(router.urls))
    
    

    
]