from django.urls import path
from .views import product_page, index_page, cat_products_page, dog_products_page

urlpatterns = [
     path('product/<int:id>/', product_page),
     path('', index_page, name='index'),
     path('cat-products', cat_products_page, name='cat-products'),
     path('dog-products', dog_products_page, name='dog-products'),

]