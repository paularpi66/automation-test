import time
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import BASE_URL

def test_add_to_cart_and_update_quantity(driver):
    product = ProductPage(driver)
    cart = CartPage(driver)

    product.go_to_product(BASE_URL, product_slug='combination-pliers')
    time.sleep(1)
    product.add_to_cart()

    product.open_cart()
    time.sleep(1)

    cart.change_quantity(3)
    time.sleep(1)

    subtotal = cart.get_subtotal_amount()
    assert subtotal is not None and subtotal > 0, 'Subtotal should be numeric and > 0 after updating qty'
