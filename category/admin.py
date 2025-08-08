from django.contrib import admin
from django.utils.html import format_html
from .models import Category

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    def thumbnal(request, object):
        return format_html('<img src = {} height= 100 width = 100>' .format(object.image.url))
    list_display=('category_name', 'slug', 'description', 'thumbnal','created_on','is_active')
    list_editable = ('is_active',)
    thumbnal.short_description = ('Image')
    prepopulated_fields = {'slug': ('category_name',)}
admin.site.register(Category, CategoryAdmin)
