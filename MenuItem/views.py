# views.py
from django.http import JsonResponse
from .utils.cart import add_to_cart, get_cart_items

def add_item_to_cart(request, item_id):
    if request.method == 'POST':
        add_to_cart(request, item_id)
        return JsonResponse({'message': 'Item added to cart.'})

def view_cart(request):
    items, total = get_cart_items(request)
    return JsonResponse({
        'items': items,
        'total': float(total)
    })
