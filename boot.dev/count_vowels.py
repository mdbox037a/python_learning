def count_vowels(message: str) -> int:
    lower_message = message.lower()
    vowels = ["a", "e", "i", "o", "u"]
    num_vowels = 0

    for char in lower_message:
        if char in vowels:
            num_vowels += 1
    return num_vowels
