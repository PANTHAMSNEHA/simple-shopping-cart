# utils/cart.py
def add_to_cart(request, item_id):
    cart = request.session.get('cart', {})
    cart[item_id] = cart.get(item_id, 0) + 1
    request.session['cart'] = cart

def get_cart_items(request):
    from ..models import MenuItem
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for item_id, quantity in cart.items():
        try:
            item = MenuItem.objects.get(id=item_id)
            items.append({
                'id': item.id,
                'name': item.name,
                'price': float(item.price),
                'quantity': quantity,
                'subtotal': float(item.price) * quantity
            })
            total += item.price * quantity
        except MenuItem.DoesNotExist:
            continue

    return items, total
