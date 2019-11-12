from django.shortcuts import render
from all_products.models import Product
from django.http import HttpResponse

# Create your views here.
def product_page(request, **kwargs):
    product=Product.objects.get(id=kwargs['id'])
    # context = {
    #     'product': Product.get_oldest_products(),
    # }
    return render(request, 'page_of_good/product.html', context={'ware': product})

def index_page(request):
    context = {
        'product': Product.get_oldest_products(),
    }
    return render(request, 'index/index.html', context=context)


def cat_products_page(request):
    products = Product.objects.filter(category_pets=1)
    return render(request, 'index/cats.html', context={'products': products})


def dog_products_page(request):
    products = Product.objects.filter(category_pets=2)
    return render(request, 'index/cats.html', context={'products': products})