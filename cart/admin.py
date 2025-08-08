from django.contrib import admin
from .models import Cart, CartItem

# Register your models here.
class CartAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        list_display = ('Cart_id','created_on','is_active')
        list_editable = ('is_active',)

admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_editable = ('quantity',)


admin.site.register(CartItem, CartAdmin)    
