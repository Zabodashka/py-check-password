import pytest
from app.main import check_password


@pytest.mark.parametrize("password", [
    "Pass@word1",
    "A1$bcdefg",
    "A1$bcdefghijklmno",
    "Valid#123",
])
def test_valid_passwords(password):
    assert check_password(password) is True


@pytest.mark.parametrize("password", [
    "qwerty",
    "Str@ng",
    "password1",
    "PASSWORD@",
    "Pass_word",
    "12345678",
    "Pass@word1 ",
    "Pässwörd1$",
    "Пароль@123",
    "A1$bcdefghijklmnop",
])
def test_invalid_passwords(password):
    assert check_password(password) is False
