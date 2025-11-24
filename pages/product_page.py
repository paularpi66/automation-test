from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.CSS_SELECTOR, 'button.single_add_to_cart_button')
    CART_LINK = (By.CSS_SELECTOR, 'a.cart-contents')

    def go_to_product(self, base_url, product_slug='combination-pliers'):
        self.visit(base_url.rstrip('/') + f'/product/{product_slug}/')

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def open_cart(self):
        self.click(*self.CART_LINK)
