from django.shortcuts import render , get_object_or_404

from . models import Category, Product

# Create your views here.

def allproducts(request, slug_cat=None):
    page_cat = None
    products = None
    if slug_cat != None:
        page_cat=get_object_or_404(Category, slug=slug_cat)
        products=Product.objects.all().filter(category=page_cat, available=True)
    else:
        products=Product.objects.all().filter(available=True)
    return render(request, 'home.html',{'category': page_cat, 'products':products})


def cat_prod(request, slug_cat=None, slug_prod=None):
    try:
        product =Product.objects.get(category__slug=slug_cat, slug=slug_prod)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product':product})