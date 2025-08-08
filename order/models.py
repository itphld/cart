from django.db import models
from account.models import Account

class Order(models.Model):
    user=models.ForeignKey(Account,null=True,blank=True,on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=20)
    address = models.CharField(max_length=150)
    total = models.IntegerField()
    tax = models.IntegerField()
    gross_total = models.IntegerField(default=1)
    ordered_on=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

def __str__(self):
  return self.first_name
