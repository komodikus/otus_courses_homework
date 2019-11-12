from django.shortcuts import render
from all_products.models import Product


# Create your views here.
def search_results(request, **kwargs):
    question = request.GET.get('q')
    products = Product.objects.filter(name_of_product__icontains=question)
    return render(request, 'search/search.html', context={'products': products})
