from django.contrib import admin
from .models import Product
from django.utils.html import format_html

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="60" height="60" style="object-fit:cover;" />', object.product_image.url)
    thumbnail.short_description = 'Image'

    list_display = ('product_name', 'slug', 'category', 'thumbnail', 'price', 'stock', 'created_on', 'is_available')
    list_editable = ('is_available',)
    prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)
# Register your models here.
