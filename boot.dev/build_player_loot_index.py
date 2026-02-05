def build_player_loot_index(drops: list[dict]) -> dict:
    loot_index = {}

    for drop in drops:
        if drop["rarity"] == "trash":
            continue

        if drop["player"] not in loot_index:
            loot_index[drop["player"]] = {}
        if drop["rarity"] not in loot_index[drop["player"]]:
            loot_index[drop["player"]][drop["rarity"]] = []
        loot_index[drop["player"]][drop["rarity"]].append(drop["item"])

    return loot_index
