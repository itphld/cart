from django.urls import path
from . import views

urlpatterns = [
   path("", views.order, name="order"),
   path("complete_order/<int:order_id>/", views.complete_order, name="complete_order"),
]
