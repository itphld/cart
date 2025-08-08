from django.shortcuts import render,get_object_or_404
from . models import Product
from category.models import Category
from django.db.models import Q
from django.core.paginator import Paginator
def store_view(request,category_slug=None):
    if category_slug!=None:
        product=Product.objects.all().filter(is_available=True,category__slug=category_slug)
        paginator = Paginator(product, 2)
        page_number = request.GET.get("page")
        pagianted_product = paginator.get_page(page_number)

        product_count=product.count()
    else:
        product=Product.objects.all().filter(is_available=True)
        paginator=Paginator(product,2)
        page_number = request.GET.get("page")
        pagianted_product = paginator.get_page(page_number)
        product_count=product.count()
    context={'product':pagianted_product,'product_count':product_count}

    return render(request, 'store.html',context)






def product_detail(request,category_slug,product_slug):
    single_product = Product.objects.get(is_available=True,category__slug=category_slug,slug=product_slug)
    context={'single_product': single_product}
    return render(request, 'product_detail.html',context)
def search(request):
    keyword = request.GET['keyword']
    if keyword:
        products = Product.objects.filter(Q(description__icontains=keyword)|Q(product_name__icontains=keyword))



        context = {'product': products,

        }





        
        return render(request, 'store.html', context)
