import string


def check_password(password: str) -> bool:
    if not (8 <= len(password) <= 16):
        return False

    allowed_specials = "$@#&!-_"
    allowed_chars = set(
        string.ascii_letters + string.digits + allowed_specials
    )

    for character in password:
        if character not in allowed_chars:
            return False

    has_upper = any(character.isupper() for character in password)
    has_digit = any(character.isdigit() for character in password)
    has_special = any(character in allowed_specials for character in password)

    return has_upper and has_digit and has_special
