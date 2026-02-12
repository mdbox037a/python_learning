def boost_scores(scores: list, bonus: int) -> list[int]:
    boosted_scores = []

    for score in scores:
        boosted_scores.append(score + bonus)

    return boosted_scores
