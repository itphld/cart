from django.db import models
from product.models import Product
from account.models import Account

# Create your models here.
class Cart(models.Model):
    Cart_id= models.CharField(max_length=100)
    created_on= models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(Account,null=True,blank=True,on_delete=models.CASCADE)
    is_active =models.BooleanField(default=True)

    def __str__(self):
       return self.Cart_id

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quentity = models.IntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.product.product_name
