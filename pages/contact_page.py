import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    CONTACT = By.CSS_SELECTOR, "a.nav-link"
    FIRST_NAME = By.ID, 'first_name'
    LAST_NAME = By.ID, 'last_name'
    EMAIL = By.ID, 'email'
    SUBJECT = By.ID, 'subject'
    MESSAGE = By.ID, 'message'
    SUBMIT = By.CSS_SELECTOR, "input.btnSubmit"
    SUCCESS = By.CSS_SELECTOR, ".alert.alert-success.mt-3"
    ERRORS = By.ID, 'first_name_alert'

    def go(self, base_url):
        self.visit(base_url)
        # try:
        #     # self.click(*self.CONTACT)
        #     print("--> 01")
        #     self.find(*self.CONTACT).click()
        #     print("--> 02")
        # except Exception:
        #     self.visit(base_url.rstrip('/') + '/contact/')
        # time.sleep(2)
        # self.wait_for_page_to_load("/contact")

    def submit_empty(self):
        # self.click(*self.SUBMIT)
        self.find(*self.SUBMIT).click()

    def fill_form(self, first_name, last_name, email, message):
        self.type(*self.FIRST_NAME, text=first_name)
        self.type(*self.LAST_NAME, text=last_name)
        self.type(*self.EMAIL, text=email)
        self.select(*self.SUBJECT, opt="Return")
        self.type(*self.MESSAGE, text=message)
        self.click(*self.SUBMIT)

    def has_validation_errors(self):
        time.sleep(2)
        els = self.driver.find_elements(*self.ERRORS)
        return len(els) > 0

    def success_message_present(self):
        try:
            return 'Thanks for your message! ' in self.text(*self.SUCCESS)
        except Exception:
            return False
