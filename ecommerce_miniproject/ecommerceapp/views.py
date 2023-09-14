from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.shortcuts import render, get_object_or_404

from ecommerceapp.models import Category, Product


# Create your views here.
def allProdCat(request, c_slug=None):
    c_page = None
    product_list = None

    # if slug is passed,display the page c_page using the slug(using slug we can find the category) or show 404 page.Then filter the products based on the category and which is available
    if c_slug is not None:
        c_page = get_object_or_404(Category, slug=c_slug)
        product_list = Product.objects.all().filter(category=c_page, available=True)



    # else show all the products irrespective of category
    else:
        product_list = Product.objects.all().filter(available=True)
    paginator = Paginator(product_list, 3)

    try:
        page = int(request.GET.get('page', '1'))

    except:
        page = 1

    try:
        product = paginator.page(page)

    except (EmptyPage, InvalidPage):
        product = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category': c_page, 'product': product})


def prodDetails(request, c_slug, p_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=p_slug)

    except Exception as e:
        raise e

    return render(request, 'product.html', {'product': product})
