import pytest
from selenium.webdriver import Firefox

from Selenium_Automation.Intro_Exercise.keyboard_actions import firefox

a=101

# Set pytest fixture (setting scope to module can make fixture occur only once, not for each TC)
@pytest.fixture(scope='module')
def set_webdriver():
    global firefox
    firefox = Firefox()
    yield
    firefox.close()

# Simple Pytest with Selenium
def test_valid_data(set_webdriver):

    firefox.get('https://www.thetestingworld.com/testings/')

# Marking test case in groups
@pytest.mark.Sanity
def test_invalid_data(set_webdriver):

    firefox.get('https://www.thetestingworld.com/testings/')

# Simple skip of a test case
# @pytest.mark.skip
def test_login(set_webdriver):
    ...

# Conditional skip of a test case
# @pytest.mark.skipif(condition=a>100, reason="Skipping test case")
def test_registration(set_webdriver):

    firefox.get('https://www.thetestingworld.com/testings/')

    # Make assertions
    assert firefox.current_url == "https://www.thetestingworld.com/testings/"
