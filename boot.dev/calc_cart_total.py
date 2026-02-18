def calculate_cart_total(cart_items, price_map):
    total = 0
    for item in cart_items:
        if item in price_map:
            total += price_map[item]
    return total
