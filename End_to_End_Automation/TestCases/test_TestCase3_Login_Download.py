import time

from selenium.webdriver.common.by import By
from Selenium_Automation.End_to_End_Automation.Library import ConfigReader
from Selenium_Automation.End_to_End_Automation.Base import base
from Selenium_Automation.End_to_End_Automation.Pages import LoginPage

def test_login_download():
    chrome = base.open_browser()

    login = LoginPage.LoginPage(chrome)
    login.navigate_to_login()
    login.enter_username('test')
    login.enter_password('test')
    login.click_login()

    chrome.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Dashboard', 'my_account_menu')).click()
    chrome.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('Dashboard', 'delete_option')).click()

    all_windows = chrome.window_handles
    main_window = ''

    for w in all_windows:
        chrome.switch_to.window(w)

        if chrome.current_url == 'https://www.thetestingworld.com/testings/manage_customer.php':
            chrome.find_element(by=By.XPATH, value=ConfigReader.get_element_locator('ManageAccount', 'download_button')).click()
            time.sleep(10)
        elif chrome.current_url == 'https://www.thetestingworld.com/testings/dashboard.php':
            main_window = w

    chrome.switch_to.window(main_window)
    base.close_browser()