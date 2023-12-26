"""
Testing user login
"""

import pytest


# Check right login/password
@pytest.mark.parametrize("expected_login, expected_password", [('qa.ajax.app.automation@gmail.com',
                                                                'qa_automation_password')])
def test_user_login(login, expected_login, expected_password):
    login_field = login()[0]
    passwd_field = login()[1]

    # enter a login and a password
    login_field.send_keys(expected_login)
    passwd_field.send_keys(expected_login)
    assert True


# Arise wrong login/password error
@pytest.mark.parametrize("wrong_login, wrong_password", [('1111@gmail.com', '0000')])
def test_user_login(before_login, after_login, wrong_login, wrong_password):
    login_field = before_login()[0]
    passwd_field = before_login()[1]

    # enter a login and a password
    login_field.send_keys(wrong_login)
    passwd_field.send_keys(wrong_password)
    after_login()
    assert False
