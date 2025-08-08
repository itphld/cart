from django.shortcuts import render,redirect
from .forms import OrderForm
from cart.views import _cart_id
from cart.models import CartItem,Cart
from decimal import Decimal
from .models import Order

# Create your views here.
def order(request):
    total=0
    tax=0
    sub_total=0
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            cart=_cart_id(request)
            cart=Cart.objects.filter(Cart_id=cart).first()
            cart_items=CartItem.objects.filter(cart=cart)
            for item in cart_items:
                total+=item.quentity*item.product.price
            tax=total* Decimal("0.2")
            sub_total=total+tax
            order=form.save(commit=False)

            order.total=total
            order.tax=tax
            order.gross_total=sub_total
            if request.user.is_authenticated:
                order.user=request.user
            order.save()
            for item in cart_items:
                item.delete()
            return redirect('complete_order',order_id=order.id)
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})
def complete_order(request,order_id):
    order=Order.objects.get(id=order_id)
    return render(request,'complete_order.html',{'order':order})
