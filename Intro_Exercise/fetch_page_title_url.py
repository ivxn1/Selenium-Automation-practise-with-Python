from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By

firefox = Firefox()
act = ActionChains(firefox)

firefox.get('https://www.thetestingworld.com/testings/')

print("Current URL is: " + firefox.current_url)
print("************************")
print("Current page title is: " + firefox.title)
print("************************")
print("Current page source is :\n" + firefox.page_source)