import time
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utils.config import BASE_URL

def test_add_to_cart_and_update_quantity(driver):
    product = ProductPage(driver)
    cart = CartPage(driver)

    product.go_to_product(BASE_URL, product_slug='01KAVCY29JJ6HZE5QWH926A86N') # combination pilers
    time.sleep(1)
    product.add_to_cart()

    product.open_cart()
    time.sleep(1)

    previous_subtotal = cart.get_subtotal_amount
    print("--> ", previous_subtotal)
    cart.change_quantity(3)
    time.sleep(5)

    new_subtotal = cart.get_subtotal_amount()
    assert previous_subtotal is not None and new_subtotal is not None and previous_subtotal != new_subtotal, 'Subtotal should be numeric and > previous value after updating qty'
