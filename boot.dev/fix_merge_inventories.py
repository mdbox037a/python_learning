# Exercise: fix merge_inventories so that it correctly sums the quantities when the same item exists in both dictionaries.
def original_merge_inventories(inv_a, inv_b):
    result = {}

    for item in inv_a:
        result[item] = inv_a[item]

    for item in inv_b:
        result[item] = inv_b[item]

    return result


def fix_merge_inventories(inv_a: dict, inv_b: dict) -> dict:
    """
    return merged inventory dictionary from two input inventories dictionaries
    if an item exists in both, the merged value should be the sum of the two input values
    """
    result = inv_a.copy()
    for item, quantity in inv_b.items():
        if item in result:
            result[item] += quantity
        else:
            result[item] = quantity

    return result
