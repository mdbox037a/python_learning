def count_vowels(text):
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
    count = 0
    vowels_found = set()
    for char in text:
        if char in vowels:
            count += 1
            vowels_found.add(char)
    return count, vowels_found
