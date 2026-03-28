
from django.urls import path
from .import views
from django.contrib import admin
urlpatterns = [
    path('home/',views.home),
    path('index/',views.index),
]

admin.site.site_title = 'Myshop'
admin.site.site_header = 'My Shopping Platform'
admin.site.index_title = 'My Shop Items'

