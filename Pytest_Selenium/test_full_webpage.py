import time

import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as ec

@pytest.fixture(scope="module")
def set_env():
    global chrome
    chrome = Chrome()

    # Set page load timeout
    # chrome.set_page_load_timeout(1)

    # Set page implicit timeout - wait until an element simply exists
    # chrome.implicitly_wait(5)

    chrome.maximize_window()
    chrome.get("https://www.thetestingworld.com/testings/")
    yield
    chrome.close()

def test_registration(set_env):
    # chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[2]').send_keys('ivan')
    # chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[3]').send_keys('abc@abc.com')
    # chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[4]').send_keys('pass123')
    # chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[5]').send_keys('pass123')
    # chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/div/input[1]').click()
    # chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[9]').click()
    time.sleep(5)
    wait = WebDriverWait(driver=chrome, timeout=100)

    wait.until(ec.text_to_be_present_in_element((By.ID, 'countryId'), 'Please wait..'))

    slct = Select(chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/select[1]'))
    slct.select_by_index(1)

    chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/div/input[2]').click()
