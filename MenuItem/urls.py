# urls.py
from django.urls import path
from .views import add_item_to_cart, view_cart

urlpatterns = [
    path('cart/add/<int:item_id>/', add_item_to_cart, name='add-to-cart'),
    path('cart/view/', view_cart, name='view-cart'),
]
