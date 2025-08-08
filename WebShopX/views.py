from django.shortcuts import render
from product.models import Product

# Create your views here.
def home(request):
    product=Product.objects.all().filter(is_available=True)
    context={'product': product}
    return render(request,'home.html',context)
