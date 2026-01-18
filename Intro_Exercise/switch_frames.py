from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By


firefox = Firefox()
firefox.get("https://www.automationtesting.co.uk/iframes.html")

firefox.switch_to.frame(firefox.find_element(by=By.XPATH, value='/html/body/div/div[1]/div/div[1]/div/iframe'))
firefox.find_element(by=By.XPATH, value='/html/body/div[2]/div/div/a[2]').click()
firefox.find_element(by=By.XPATH,value='//*[@id="banner"]/div/header/p[2]/a').click()

firefox.switch_to.default_content()
print(firefox.find_element(by=By.XPATH,value='//*[@id="main"]/div/h2').text)
firefox.close()