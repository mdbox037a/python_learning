def filter_long_words(words: list[str], min_length: int):
    long_words = []
    if min_length == 0 or min_length == 1:
        return words
    for word in words:
        if len(word) >= min_length:
            long_words.append(word)
    return long_words
