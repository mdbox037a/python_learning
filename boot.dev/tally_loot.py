def tally_loot(loot_items):
    counts = {}
    for item in loot_items:
        if item not in counts:
            counts[item] = 0
        counts[item] = 1
    return counts
