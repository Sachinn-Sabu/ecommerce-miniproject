from django.db.models import Q
from django.shortcuts import render
from ecommerceapp.models import Product

# Create your views here.
def SearchResult(request):
    query = None
    products = None

    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.filter(Q(name__icontains=query))

    return render(request, 'search.html', {'query': query, 'products': products})
