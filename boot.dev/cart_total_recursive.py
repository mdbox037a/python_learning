def cart_total_recursive(prices: list[int]):
    total = 0
    if len(prices) == 0:
        return 0
    else:
        total += prices.pop(-1) + cart_total_recursive(prices)
    return total
