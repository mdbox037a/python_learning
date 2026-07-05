def tally_loot(loot_items):
    counts = {}
    for item in loot_items:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    print_counts(counts)
    return counts

def print_counts(counts: dict):
    for item in counts:
        print(f"{item}: {counts[item]}")
    return
