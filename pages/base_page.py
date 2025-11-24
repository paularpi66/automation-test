from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def visit(self, url):
        self.driver.get(url)
    
    def wait_for_page_to_load(self, new_url,timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(new_url))

    def find(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def click(self, by, value, timeout=10):
        el = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        el.click()

    def type(self, by, value, text, timeout=10):
        el = self.find(by, value, timeout)
        el.clear()
        el.send_keys(text)

    def text(self, by, value, timeout=10):
        el = self.find(by, value, timeout)
        return el.text
