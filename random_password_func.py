import random
import secrets
import string


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