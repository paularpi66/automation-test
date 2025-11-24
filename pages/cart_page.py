from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    QTY_INPUT = (By.CSS_SELECTOR, "td.col-md-2.align-middle > input[data-test='product-quantity']")
    PRICE = (By.CSS_SELECTOR, "td.col-md-2.text-end > span[data-test='price-value']")
    SUBTOTAL = (By.CSS_SELECTOR, "td.col-md-2.text-end > span[data-test='line-price'")

    def change_quantity(self, qty):
        q = self.find(*self.QTY_INPUT)
        q.clear()
        q.send_keys(str(qty))
        # self.click(*self.UPDATE_BTN)

    def get_subtotal_amount(self):
        txt = self.text(*self.SUBTOTAL)
        clean = ''.join(ch for ch in txt if (ch.isdigit() or ch == '.'))
        try:
            return float(clean)
        except Exception:
            return None
