from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
from Selenium_Automation.End_to_End_Automation.Library import ConfigReader

def open_browser(url='https://www.thetestingworld.com/testings/index.php'):
    global browser

    if (ConfigReader.read_config('Details', 'browser')).lower() == 'chrome':
        browser = Chrome()
    elif (ConfigReader.read_config('Details', 'browser')).lower() == 'firefox':
        browser = Firefox()
    else:
        browser = Chrome()

    browser.get(url)
    browser.maximize_window()
    return browser

def close_browser():
    browser.close()
