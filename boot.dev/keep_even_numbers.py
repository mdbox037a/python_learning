def keep_even_numbers(numbers):
    only_evens = []

    for num in numbers:
        if num % 2 == 0:
            only_evens.append(num)
    return only_evens
