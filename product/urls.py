from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_view, name='store_view'),
    path('category/<slug:category_slug>/', views.store_view, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
    path('search/',views.search,name='search'),

]
