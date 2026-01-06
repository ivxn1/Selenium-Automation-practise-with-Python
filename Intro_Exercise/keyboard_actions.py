from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox = Firefox()

firefox.get("https://thetestingworld.com/testings/")

firefox.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[2]').send_keys('ivan')

act = ActionChains(firefox)

# Click on keyboard button
# act.send_keys(Keys.TAB).perform()

# Combination of multiple keyboard buttons
act.key_down(Keys.COMMAND).send_keys('A').send_keys(Keys.BACKSPACE).perform()
