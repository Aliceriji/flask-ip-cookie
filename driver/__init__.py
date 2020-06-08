from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class DRIVER:

    def __init__(self):
        self.driver =  webdriver.Chrome()

    def del_driver(self):
        self.driver.close()

    def Ret_driver(self):
        return self.driver

class PREFS_DRIVER(DRIVER):

    def __init__(self):
        chrome_options = Options()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

class HEADLESS_DRIVER(DRIVER):

    def __init__(self):
        chrome_options = Options()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)

class LINUX_DRIVER(DRIVER):

    def __init__(self):
        chrome_options = Options()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_argument('--headless')
        chrome_options.add_experimental_option('prefs', prefs)
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-gpu')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome('chromedriver', chrome_options=chrome_options)