import pytest
from app.main import check_password

@pytest.mark.parametrize("password", [
    "Pass@word1",
    "A1$bcdefg",
    "A1$bcdefghijklmn",
    "Valid#123",
])
def test_valid_passwords(password):
    assert check_password(password) is True


@pytest.mark.parametrize("password", [
    "A1$a",  # too short
    "A1$" + "a" * 14 + "b",  # 17 chars
])
def test_invalid_length(password):
    assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "Password!",     # no digit
    "Strong#Pass",
])
def test_missing_digit(password):
    assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "pass@word1",    # no uppercase
    "valid#123",
])
def test_missing_uppercase(password):
    assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "Password1",     # no special char
    "A1b2c3d4",
])
def test_missing_special_char(password):
    assert check_password(password) is False


@pytest.mark.parametrize("password", [
    "Pass word1!",     # space
    "Pass*word1",      # * is not allowed
    "Päss@word1",      # non-latin ä
    "Пароль@123",      # Cyrillic
])
def test_disallowed_characters(password):
    assert check_password(password) is False
