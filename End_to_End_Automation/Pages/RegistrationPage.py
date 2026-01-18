from selenium.webdriver.common.by import By
from Selenium_Automation.End_to_End_Automation.Library import ConfigReader

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration', 'username_field')).send_keys(username)

    def enter_email(self, email):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration', 'email_field')).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration', 'password_field')).send_keys(password)

    def enter_confirm_password(self, password):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Registration','confirm_password_field')).send_keys(password)
