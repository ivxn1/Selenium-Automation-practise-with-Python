from selenium.webdriver import Firefox, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox = Firefox()
main_win = None
firefox.get("https://www.dummysoftware.com/popupdummy_testpage.html")

# firefox.find_element(by=By.XPATH, value='/html/body/table[2]/tbody/tr/td[2]/p[1]/table/tbody/tr/td[2]/font[1]/input').click()

all_windows = firefox.window_handles

for w in all_windows:
    firefox.switch_to.window(w)
    if firefox.current_url == "https://www.dummysoftware.com/popupdummy_testpage.html":
        print("main page")
        main_win = w
    else:
        firefox.close()

firefox.switch_to.window(main_win)
firefox.close()