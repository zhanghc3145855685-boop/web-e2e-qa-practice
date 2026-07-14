from playwright.sync_api import Page

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"


def test_smoke_checkout_to_complete(page: Page, base_url: str) -> None:
    """4.2.5（可选）完成一次结账到成功页"""
    LoginPage(page, base_url).login("standard_user", PASSWORD)
    inventory = InventoryPage(page, base_url)
    inventory.expect_loaded()
    inventory.add_backpack_to_cart()
    inventory.open_cart()

    cart = CartPage(page, base_url)
    cart.expect_loaded()
    cart.checkout()

    checkout = CheckoutPage(page, base_url)
    checkout.fill_info("Auto", "Smoke", "100000")
    checkout.continue_to_overview()
    checkout.finish()
    checkout.expect_complete()
