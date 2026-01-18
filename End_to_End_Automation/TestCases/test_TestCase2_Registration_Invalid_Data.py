from selenium.webdriver.common.by import By

from Selenium_Automation.End_to_End_Automation.Base import base

def test_invalid_registration():
    chrome = base.open_browser()
    chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[2]').send_keys('ivan')
    chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[3]').send_keys('abc@abc')
    chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[4]').send_keys('pass123')
    chrome.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[5]').send_keys('pass123')
    base.close_browser()