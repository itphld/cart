from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=500)
    image = models.ImageField(upload_to='Image/')
    created_on=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.category_name
    def get_urls(self):
        return reverse('products_by_category', args=[self.slug])
