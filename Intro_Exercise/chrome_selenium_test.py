from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = Chrome(options=chrome_options)

driver.get('https://www.thetestingworld.com/testings/')

driver.maximize_window()
driver.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[2]').send_keys('ivan')
driver.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[3]').send_keys('abc@abc.com')
driver.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[4]').send_keys('pass123')
driver.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[5]').send_keys('pass123')
driver.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/div/input[1]').click()
driver.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/input[9]').click()

slct = Select(driver.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/select[1]'))
slct.select_by_index(1)

# driver.find_element(by=By.XPATH,value='//*[@id="tab-content1"]/form/div/input[2]').click()
