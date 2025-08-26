import string


def check_password(password: str) -> bool:
    if not (8 <= len(password) <= 16):
        return False

    allowed_specials = "$@#&!-_;"
    allowed_chars = set(
        string.ascii_letters + string.digits + allowed_specials
    )

    for char in password:
        if char not in allowed_chars:
            return False

    has_upper = any(char.isupper() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_special = any(char in allowed_specials for char in password)

    return has_upper and has_digit and has_special
