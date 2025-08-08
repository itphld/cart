from django.shortcuts import render,redirect
from product.models import Product
from .models import Cart,CartItem
from django.http import HttpResponse
from decimal import Decimal
from order.forms import OrderForm



# Create your views here.
def _cart_id(request):
    if request.user.is_authenticated:
        cart,created=Cart.objects.get_or_create(user=request.user)
        return cart
    else:


        session_key=request.session.session_key
        if not session_key:
            request.session.create()
            session_key=request.session.session_key
        cart=Cart.objects.get_or_create(Cart_id=session_key,is_active=True)
        return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(Cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(Cart_id=_cart_id(request),is_active=True)
        cart.save()
    try:
        cart_item=CartItem.objects.get(cart=cart,product=product)
        cart_item.quentity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(cart=cart,product=product,quentity=1)
        cart_item.save()
    #return HttpResponse('great!')

    return redirect('cart')

def delete_cart(request,product_id,cart_item_id):
    cart=Cart.objects.get(Cart_id=_cart_id(request))

    product=Product.objects.get(id=product_id)
    cart_item=CartItem.objects.get(cart=cart,product=product,id=cart_item_id)
    if cart_item.quentity >=1:
        cart_item.quentity-=1
        cart_item.save()

    else:
        cart_item.delete()
    return redirect('cart')
def remove_cart(request,product_id,cart_item_id):
    cart=Cart.objects.get(Cart_id=_cart_id(request))

    product=Product.objects.get(id=product_id)
    cart_item=CartItem.objects.get(cart=cart,product=product,id=cart_item_id)
    cart_item.delete()
    return redirect('cart')
def cart(request):
    total=0
    tax = Decimal('0.0')
    gross_total=0


    cart=Cart.objects.get(Cart_id=_cart_id(request))
    cart_item=CartItem.objects.filter(cart=cart)
    for cartitem in cart_item:
        total+=cartitem.quentity*cartitem.product.price
        cartitem.total_sum=cartitem.quentity*cartitem.product.price
    tax=total * Decimal('0.2')
    gross_total=total+tax




    context={'cart_item':cart_item,'total':total,'tax':tax,'gross_total':gross_total}
    return render(request, 'cart.html',context)
def cart(request):
    total=0
    tax = Decimal('0.0')
    gross_total=0


    cart=Cart.objects.get(Cart_id=_cart_id(request))
    cart_item=CartItem.objects.filter(cart=cart)
    for cartitem in cart_item:
        total+=cartitem.quentity*cartitem.product.price
        cartitem.total_sum=cartitem.quentity*cartitem.product.price
    tax=total * Decimal('0.2')
    gross_total=total+tax




    context={'cart_item':cart_item,'total':total,'tax':tax,'gross_total':gross_total}
    return render(request, 'cart.html',context)
def cart(request):
    total=0
    tax = Decimal('0.0')
    gross_total=0


    cart=Cart.objects.filter(Cart_id=_cart_id(request)).first()
    cart_item=CartItem.objects.filter(cart=cart)
    for cartitem in cart_item:
        total+=cartitem.quentity*cartitem.product.price
        cartitem.total_sum=cartitem.quentity*cartitem.product.price
    tax=total * Decimal('0.2')
    gross_total=total+tax




    context={'cart_item':cart_item,'total':total,'tax':tax,'gross_total':gross_total}
    return render(request, 'cart.html',context)
def place_order(request):
    total=0
    tax = Decimal('0.0')
    gross_total=0


    cart=Cart.objects.get(Cart_id=_cart_id(request))
    cart_item=CartItem.objects.filter(cart=cart)
    for cartitem in cart_item:
        total+=cartitem.quentity*cartitem.product.price
        cartitem.total_sum=cartitem.quentity*cartitem.product.price
    tax=total * Decimal('0.2')
    gross_total=total+tax
    form=OrderForm()




    context={'cart_item':cart_item,'total':total,'tax':tax,'gross_total':gross_total,'form':form}
    return render(request, 'place_order.html',context)
