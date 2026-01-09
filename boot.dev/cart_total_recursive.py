def cart_total_recursive(prices: list[int]) -> int:
    if len(prices) == 0:
        return 0
    return prices[0] + cart_total_recursive(prices[1:])
