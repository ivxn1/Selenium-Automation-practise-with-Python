from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By

firefox = Firefox()
act = ActionChains(firefox)

firefox.get('https://www.thetestingworld.com/testings/')

print("Link's inner text is: " + firefox.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/div/em/a').text)
print("***************")
print("Value of Sign up button is: "
      +
      firefox.find_element(
          by=By.XPATH,
          value='//*[@id="tab-content1"]/form/div/input[2]').get_attribute('value')
      )