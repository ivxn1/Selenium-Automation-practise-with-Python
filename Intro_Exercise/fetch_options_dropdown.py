from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

firefox = Firefox()
act = ActionChains(firefox)

firefox.get('https://www.thetestingworld.com/testings/')

dropdown = Select(firefox.find_element(by=By.XPATH, value='//*[@id="tab-content1"]/form/select[1]'))

# Print currently selected option
# dropdown.select_by_index(1)
# print(dropdown.first_selected_option.text)

# Print all possible options
for op in dropdown.options:
    print(op.text)