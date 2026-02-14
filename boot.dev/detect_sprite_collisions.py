import copy


def advance_one_frame(sprites: list[dict], velocities: dict, fps: int) -> list[dict]:
    """
    Move sprites forward by one frame, per their volocities, and return a new
    list with updated positions for each
    """
    updated_sprites = copy.deepcopy(sprites)

    for sprite in updated_sprites:
        sprite["rect"] = (
            sprite["rect"][0] + velocities[sprite["id"]][0] // fps,
            sprite["rect"][1] + velocities[sprite["id"]][1] // fps,
            sprite["rect"][2],
            sprite["rect"][3],
        )

    return updated_sprites


def detect_collisions(bullets: list[dict], enemies: list[dict]) -> list[tuple]:
    """
    Given two sprite groups, determine if any are currently overlapping, and
    return a list of tuples of overlapping pairs
    """
    overlaps = []

    for bullet in bullets:
        for enemy in enemies:
            if (
                bullet["rect"][0] < enemy["rect"][0] + enemy["rect"][2]
                and bullet["rect"][0] + bullet["rect"][2] > enemy["rect"][0]
                and bullet["rect"][1] < enemy["rect"][1] + enemy["rect"][3]
                and bullet["rect"][1] + bullet["rect"][3] > enemy["rect"][1]
            ):
                overlaps.append((bullet["id"], enemy["id"]))

    return overlaps
