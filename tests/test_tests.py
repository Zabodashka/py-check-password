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
    "short1!",        # меньше 8 символов
    "toolongpassword1$!",  # больше 16 символов
    "NoSpecialChar1", # нет спецсимвола
    "nospecialchar1", # нет заглавной буквы и спецсимвола
    "NoDigit!@",      # нет цифры
    "InvalidChar%1A", # недопустимый символ %
])
def test_invalid_passwords(password):
    assert check_password(password) is False
