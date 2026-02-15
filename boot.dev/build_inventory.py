def build_inventory(items: list[str]) -> dict:
    inventory = {}

    for item in items:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory[item] = 1

    return inventory
