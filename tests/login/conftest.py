import pytest
from dev_in_test_app_team import framework as f


# To take a driver and return login functionality
@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield f.login_page.LoginPage(driver)


# To prepare field to enter in
@pytest.fixture(scope='function')
def before_login(user_login_fixture):
    # enter login button's class
    log_button = user_login_fixture.find_element("login_button_class")

    # open login page
    user_login_fixture.click_element(log_button)

    # find login's and password's fields
    login_field = user_login_fixture.find_element("login_field")
    passwd_field = user_login_fixture.find_element("passwd_field")
    return login_field, passwd_field


# To send entered into fields values
@pytest.fixture(scope='function')
def after_login(user_login_fixture):
    yield

    # Find "Log in" button
    btn = user_login_fixture.find_element("login_send_button")

    # Send values
    return user_login_fixture.click_element(btn)
