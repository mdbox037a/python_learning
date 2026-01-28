def combine_inventories(inv1: dict, inv2: dict) -> dict:
    combined_inv = {}
    combined_inv.update(inv1)
    for item in inv2:
        if item in combined_inv:
            combined_inv[item] += inv2[item]
        else:
            combined_inv[item] = inv2[item]
    return combined_inv
