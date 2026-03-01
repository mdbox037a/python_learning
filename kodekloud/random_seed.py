import random


def random_seed(user_seed: float) -> float:
    random.seed(user_seed)
    return random.random()


s = float(input("Enter a value: "))
print(random_seed(s))
