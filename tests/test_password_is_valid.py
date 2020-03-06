import pytest
from password_checker.password_check import Password_Checker

password = "eof87PQz#"

password_Checker = Password_Checker(password)

def test_lowercase():
    assert password_Checker.lowercase(password)==True
def test_uppercase():
    assert password_Checker.uppercase(password)==True
def test_num_digits():
    assert password_Checker.num_digits(password)==True
def test_special_charectors():
    assert password_Checker.special_charectors(password)==True
def test_password_is_valid():
    assert password_Checker.password_is_valid(password)==True

   