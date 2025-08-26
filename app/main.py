import string


def check_password(password: str) -> bool:
    if not (8 <= len(password) <= 16):
        return False

    allowed_specials = "$@#&!-_;"
    allowed_chars = set(
        string.ascii_letters + string.digits + allowed_specials
    )

    # Проверка на допустимые символы
    for c in password:
        if c not in allowed_chars:
            return False

    # Проверка на наличие хотя бы одного символа каждого типа
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in allowed_specials for c in password)

    return has_upper and has_digit and has_special
