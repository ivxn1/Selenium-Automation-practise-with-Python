from selenium.webdriver.common.by import By
from Selenium_Automation.End_to_End_Automation.Library import ConfigReader

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login(self):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Login', 'login_link')).click()

    def enter_username(self, username):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Login', 'username_field')).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Login', 'password_field')).send_keys(password)

    def click_login(self):
        self.driver.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Login', 'login_button')).click()