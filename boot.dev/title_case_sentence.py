def title_case_sentence(sentence: str):
    words = sentence.split(" ")
    tc_words = []
    for word in words:
        tc_words.append(word.capitalize())
    return " ".join(tc_words)
