import logging
from selenium.webdriver import Firefox, ActionChains

log = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', encoding='utf-8', level=logging.INFO)

warn = logging.FileHandler('Warning_Logs')
warn.setLevel(logging.WARNING)

info = logging.FileHandler('Info_Logs')
info.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime) - %(levelname) - %(name)')

info.setFormatter(formatter)
warn.setFormatter(formatter)

log.info('This is info')
log.warning('There is a delay')

firefox = Firefox()
firefox.get('https://www.thetestingworld.com/testings/')

