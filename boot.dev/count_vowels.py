def count_vowels(message: str) -> int:
    lower_message = message.lower()
    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0

    for char in lower_message:
        if char in vowels:
            num_vowels += 1
    return num_vowels


def count_consonants(message: str) -> int:
    lower_message = message.lower()
    other = [
        "!",
        "?",
        ".",
        " ",
    ]
    vowels = ["a", "e", "i", "o", "u"]
    num_consonants = 0

    for char in lower_message:
        if char not in vowels or char not in other:
            num_consonants += 1
    return num_consonants
