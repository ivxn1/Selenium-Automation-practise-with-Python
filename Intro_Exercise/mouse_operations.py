from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox = Firefox()
act = ActionChains(firefox)

# firefox.get("https://thetestingworldapi.com/")
#
# # Simple left click
# act.click(firefox.find_element(by=By.XPATH, value='//html/body/div[1]/div/div[2]/ul/li[2]/a')).perform()
#
# # Simple right click
# act.context_click().perform()

# Double click
# firefox.get('https://www.thetestingworld.com/testings/')
# act.double_click(firefox.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/div/input[1]')).perform()

# Hover
# firefox.get('https://www.webpagetest.org/')
# act.move_to_element(firefox.find_element(by=By.XPATH, value='//*[@id="w-dropdown-toggle-0"]')).perform()




