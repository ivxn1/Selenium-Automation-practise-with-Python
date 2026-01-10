from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox = Firefox()
firefox.get("https://www.thetestingworld.com/testings/index.php")

firefox.find_element(by=By.XPATH, value='/html/body/div[4]/section/ul/li[2]/label').click()

firefox.find_element(by=By.XPATH, value='//*[@id="tab-content2"]/form/input[2]').send_keys('test')
firefox.find_element(by=By.XPATH, value='//*[@id="tab-content2"]/form/input[3]').send_keys('test')

firefox.find_element(by=By.XPATH,value='//*[@id="tab-content2"]/form/div/input[2]').click()

firefox.find_element(by=By.XPATH,value='//*[@id="navbar-brand-centered"]/ul/li[2]/a').click()
firefox.find_element(by=By.XPATH,value='//*[@id="navbar-brand-centered"]/ul/li[2]/ul/li[6]/a').click()

all_w = firefox.window_handles


for w in all_w:
    firefox.switch_to.window(w)
    if firefox.current_url == 'https://www.thetestingworld.com/testings/manage_customer.php':
        firefox.find_element(by=By.ID, value='downloadButton').click()

