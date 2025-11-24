from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    CONTACT = (By.CSS_SELECTOR, "a.nav-link")
    NAME = (By.ID, 'name')
    EMAIL = (By.ID, 'email')
    MESSAGE = (By.ID, 'message')
    SUBMIT = (By.CSS_SELECTOR, "input.btnSubmit")
    SUCCESS = (By.CSS_SELECTOR, '.wpcf7-mail-sent-ok')
    ERRORS = (By.CSS_SELECTOR, '.wpcf7-not-valid')

    def go(self, base_url):
        self.visit(base_url)
        try:
            # self.click(*self.CONTACT)
            print("--> 01")
            self.find(*self.CONTACT).click()
            print("--> 02")
        except Exception:
            self.visit(base_url.rstrip('/') + '/contact/')
        self.wait_for_page_to_load("/contact")

    def submit_empty(self):
        # self.click(*self.SUBMIT)
        self.find(*self.SUBMIT).click()

    def fill_form(self, name, email, message):
        self.type(*self.NAME, text=name)
        self.type(*self.EMAIL, text=email)
        self.type(*self.MESSAGE, text=message)
        self.click(*self.SUBMIT)

    def has_validation_errors(self):
        els = self.driver.find_elements(*self.ERRORS)
        return len(els) > 0

    def success_message_present(self):
        try:
            return 'Thank you' in self.text(*self.SUCCESS)
        except Exception:
            return False
