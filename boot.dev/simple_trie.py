END_SYMBOL = "*"


def insert_word(trie, word):
    current = trie
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]
    current[END_SYMBOL] = True


def contains_word(trie, word):
    current = trie
    for char in word:
        if char not in current:
            return False
        current = current[char]
    if END_SYMBOL in current:
        return True
    else:
        return False
