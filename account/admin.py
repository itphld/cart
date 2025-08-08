from django.contrib import admin
from .models import Account
#ist_display = ('first_name', 'last_name', 'mobile', 'email', 'is_active')

    #list_editable = ('is_active',)



admin.site.register(Account)
# Register your models here.
