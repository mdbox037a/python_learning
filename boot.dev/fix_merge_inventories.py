# Exercise: fix merge_inventories so that it correctly sums the quantities when the same item exists in both dictionaries.
def merge_inventories(inv_a, inv_b):
    result = {}

    for item in inv_a:
        result[item] = inv_a[item]

    for item in inv_b:
        result[item] = inv_b[item]

    return result
