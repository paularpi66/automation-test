from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from .config import BROWSER, HEADLESS, IMPLICIT_WAIT

def create_driver():
    if BROWSER == 'firefox':
        opts = FirefoxOptions()
        if HEADLESS:
            opts.add_argument('--headless')
        service = FirefoxService()
        driver = webdriver.Firefox(service=service, options=opts)
    else:
        opts = ChromeOptions()
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-dev-shm-usage')
        if HEADLESS:
            opts.add_argument('--headless=new')
        service = ChromeService()
        driver = webdriver.Chrome(service=service, options=opts)

    driver.implicitly_wait(IMPLICIT_WAIT)
    try:
        driver.maximize_window()
    except Exception:
        pass
    return driver
