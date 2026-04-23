#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Лёгкий рандомайзер: числа, никнеймы, пароли, креативные фразы.
Запуск: python randomizer_app.py
"""

from __future__ import annotations

import random
import secrets
import string


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


# --- 2. Случайные никнеймы ---


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


# --- 3. Случайные пароли ---


def random_password(
    length: int = 16,
    use_upper: bool = True,
    use_lower: bool = True,
    use_digits: bool = True,
    use_symbols: bool = True,
) -> str:
    """Генерирует пароль из букв, цифр и безопасных символов (secrets)."""
    if length < 4:
        raise ValueError("Минимальная длина пароля — 4.")
    alphabet = ""
    if use_lower:
        alphabet += string.ascii_lowercase
    if use_upper:
        alphabet += string.ascii_uppercase
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%&*-_=+?"
    if not alphabet:
        raise ValueError("Нужно включить хотя бы один тип символов.")
    # гарантируем хотя бы один символ каждого включённого типа
    required: list[str] = []
    if use_lower:
        required.append(secrets.choice(string.ascii_lowercase))
    if use_upper:
        required.append(secrets.choice(string.ascii_uppercase))
    if use_digits:
        required.append(secrets.choice(string.digits))
    if use_symbols:
        required.append(secrets.choice("!@#$%&*-_=+?"))
    rest_len = max(0, length - len(required))
    body = [secrets.choice(alphabet) for _ in range(rest_len)]
    chars = required + body
    random.shuffle(chars)
    return "".join(chars[:length])


# --- 4. Креативные предложения ---


_SUBJECTS = (
    "кот-программист", "робот-бариста", "облако из пикселей",
    "старый роутер", "пингвин в наушниках", "чайник с Wi‑Fi",
    "нейросеть в отпуске", "баг, который стал фичей",
)
_VERBS = (
    "украл у вселенной", "переписал законы физики ради", "спрятал в кэше",
    "забронировал столик на Марсе для", "написал haiku про", "подписал NDA с",
)
_OBJECTS = (
    "секретный рецепт пельменей", "последний бит свободной RAM",
    "радугу в HEX", "архив из снов", "одинокий NULL", "загрузочный экран вечности",
)
_MOODS = (
    "и это было прекрасно.", "никто об этом не узнает.", "потом все смеялись.",
    "историки до сих пор спорят.", "а завтра — новый спринт.",
)


def random_creative_sentence() -> str:
    """Собирает абсурдное, но грамотное предложение из шаблонных кусков."""
    s = (
        f"{secrets.choice(_SUBJECTS).capitalize()} "
        f"{secrets.choice(_VERBS)} "
        f"{secrets.choice(_OBJECTS)}, "
        f"{secrets.choice(_MOODS)}"
    )
    return s


def random_creative_paragraph(sentences: int = 3) -> str:
    """Несколько креативных предложений подряд."""
    return " ".join(random_creative_sentence() for _ in range(max(1, sentences)))


def main() -> None:
    print("=== Рандомайзер ===\n")
    while True:
        print(
            "1 — случайные числа\n"
            "2 — никнейм\n"
            "3 — пароль\n"
            "4 — креативный текст\n"
            "0 — выход"
        )
        choice = input("Выбор: ").strip()
        if choice == "0":
            print("Пока!")
            break
        if choice == "1":
            n = int(input("Сколько чисел (по умол. 5): ") or "5")
            a = int(input("От (по умол. 1): ") or "1")
            b = int(input("До (по умол. 100): ") or "100")
            u = input("Только уникальные? y/N: ").strip().lower() == "y"
            print(random_numbers(n, a, b, u))
        elif choice == "2":
            print(random_nickname())
        elif choice == "3":
            ln = int(input("Длина пароля (по умол. 16): ") or "16")
            print(random_password(ln))
        elif choice == "4":
            k = int(input("Сколько предложений (по умол. 3): ") or "3")
            print(random_creative_paragraph(k))
        else:
            print("Неизвестный пункт.\n")
            continue
        print()


if __name__ == "__main__":
    main()
