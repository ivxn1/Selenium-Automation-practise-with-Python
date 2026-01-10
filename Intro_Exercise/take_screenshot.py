from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get("https://thetestingworld.com/testings/")
firefox.get_screenshot_as_file('/Users/ivanzhelev/Documents/PersonalProjects/Selenium_Automation/Intro_Exercise/sc.png')