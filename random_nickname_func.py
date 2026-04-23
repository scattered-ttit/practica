import random
import secrets

_PREFIXES = (
    "Shadow", "Neon", "Pixel", "Lunar", "Frost", "Cyber", "Silent", "Wild",
    "Tiny", "Iron", "Golden", "Crimson", "Azure", "Storm", "Echo", "Nova",
)
_SUFFIXES = (
    "Wolf", "Fox", "Bear", "Owl", "Hawk", "Drake", "Knight", "Ghost",
    "Byte", "Wave", "Spark", "Blade", "Star", "Moon", "Void", "Rune",
)


def random_nickname(with_digits: bool = True) -> str:
    """Собирает ник из префикса, суффикса и опционально короткого числа."""
    base = f"{secrets.choice(_PREFIXES)}{secrets.choice(_SUFFIXES)}"
    if with_digits and random.random() < 0.6:
        base += str(random.randint(10, 9999))
    return base