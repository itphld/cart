from django.db.models import Sum
from .models import Cart,CartItem
from .views import _cart_id


def cart_counts(request):
    cart_count=0
    cartitem=CartItem.objects.filter(cart__Cart_id=_cart_id(request))
    cart_count=cartitem.aggregate(Sum('quentity'))['quentity__sum'] or 0
    return dict(cart_count=cart_count)
