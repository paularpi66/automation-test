from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, 'btn-add-to-cart')
    CART_LINK = (By.XPATH, "//a[@class='nav-link'][./span[@id='lblCartCount']]")

    def go_to_product(self, base_url, product_slug='01KAVCY29JJ6HZE5QWH926A86N'):
        product_url = base_url.rstrip('/') + f'/product/{product_slug}/'
        self.visit(product_url)
        self.wait_for_page_to_load(product_slug)

    def add_to_cart(self):
        self.find(*self.ADD_TO_CART)
        print("cart button found")
        self.click(*self.ADD_TO_CART)

    def open_cart(self):
        self.click(*self.CART_LINK)
        self.wait_for_page_to_load("/checkout")
