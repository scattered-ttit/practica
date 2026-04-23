import random

# --- 1. Случайные числа ---


def random_numbers(
    count: int = 5,
    low: int = 1,
    high: int = 100,
    unique: bool = False,
) -> list[int]:
    """Возвращает список из count случайных целых чисел в диапазоне [low, high]."""
    if low > high:
        low, high = high, low
    span = high - low + 1
    if unique and count > span:
        raise ValueError("Нельзя выдать столько уникальных чисел в заданном диапазоне.")
    if unique:
        return random.sample(range(low, high + 1), count)
    return [random.randint(low, high) for _ in range(count)]

