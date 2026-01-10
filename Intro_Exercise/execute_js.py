from selenium.webdriver import Firefox

firefox = Firefox()

firefox.get("https://thetestingworld.com/testings/")
firefox.execute_script("window.scrollTo(0, 400);")