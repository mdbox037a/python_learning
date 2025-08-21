def remove_duplicates(spells):
    seen = set()
    deduped_spells = []
    for spell in spells:
        if spell not in seen:
            seen.add(spell)
            deduped_spells.append(spell)
    return deduped_spells


def alt_remove_duplicates(spells):
    return list(set(spells))
