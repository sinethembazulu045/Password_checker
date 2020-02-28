import pytest
from password_checker.password_checker import Password_Checker

def test_password_is_valid():
    with pytest.raises(Exception) as e:
        password = "qwe#5K2yd"
        password_checker = Password_Checker(password)
        assert Password_Checker.password_is_valid(password)
    assert str(e.value) == 'length of the password should be more than 8'

    # assert password_checker.password_is_valid(password)==True
    # assert password_checker.lowercase(password)==True
    # assert password_checker.uppercase(password)==True
    # assert password_checker.num_digits(password)==True
    # assert password_checker.special_charectors(password)==True
  
   