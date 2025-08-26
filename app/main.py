import string


def check_password(password: str) -> bool:
    if not (8 <= len(password) <= 16):
        return False

    allowed_specials = "$@#&!-_;"
    allowed_chars = set(string.ascii_letters + string.digits + allowed_specials)

    # Проверка на наличие только допустимых символов
    if not all(c in allowed_chars for c in password):
        return False

    # Проверка на наличие заглавной буквы
    if not any(c.isupper() for c in password):
        return False

    # Проверка на наличие цифры
    if not any(c.isdigit() for c in password):
        return False

    # Проверка на наличие специального символа
    if not any(c in allowed_specials for c in password):
        return False

    return True
