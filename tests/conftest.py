"""
Setting up the environment for testing.
"""

import subprocess
import time

import pytest
from appium import webdriver

from appium.webdriver.webdriver import AppiumOptions
from dev_in_test_app_team import utils as u


# Launch Appium Server {'host': '0.0.0.0', 'port': 4723} before the testing
@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True,
    )

    # Dynamically getting aan udid of a first connected device
    udid_get = subprocess.Popen("adb devices -l | cut -d ' ' -f 1 | cut -d 'L' -f 1",
                                shell=True)
    udid, errors = udid_get.communicate()
    time.sleep(5)
    return udid


# Launch WebDriver for connecting to device and application
@pytest.fixture(scope='session')
def driver(run_appium_server):
    options = AppiumOptions().load_capabilities(u.android_utils.android_get_desired_capabilities())
    options.set_capability("udid", run_appium_server())
    driver = webdriver.Remote(command_executor='http://localhost:4723/wd/hub', options=options)
    yield driver


# TODO: Handle an error with driver connection
