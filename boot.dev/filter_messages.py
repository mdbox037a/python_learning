def filter_messages(messages):
    filtered = []
    count = []

    for message in messages:
        good_words = []
        dangs = []

        for item in message.split():
            if item == "dang":
                dangs.append(item)
            else:
                good_words.append(item)

        filtered.append(" ".join(good_words))
        count.append(len(dangs))

    return filtered, count
