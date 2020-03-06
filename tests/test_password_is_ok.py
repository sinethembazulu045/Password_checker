from password_checker.password_checker import Password_Checker
password = "epQz#"
password_checker = Password_Checker(password)

def test_password_is_ok():
    assert password_checker.password_is_ok(password)==True
 