from selenium.webdriver.common.by import By
from Selenium_Automation.End_to_End_Automation.Base.base import open_browser, close_browser
from Selenium_Automation.End_to_End_Automation.Library import ConfigReader

def test_Validate_Registration():

    browser = open_browser()

    browser.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration', 'username_field')).send_keys('ivan')
    browser.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration', 'email_field')).send_keys('ivan@ivan.com')
    browser.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration', 'password_field')).send_keys('123')
    browser.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration', 'confirm_password_field')).send_keys('123')

    close_browser()

