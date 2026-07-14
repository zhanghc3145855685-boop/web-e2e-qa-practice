from playwright.sync_api import Page, expect

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"


def test_smoke_add_item_and_open_cart(page: Page, base_url: str) -> None:
    """4.2.4 加购一件商品并进入购物车"""
    LoginPage(page, base_url).login("standard_user", PASSWORD)
    inventory = InventoryPage(page, base_url)
    inventory.expect_loaded()
    inventory.add_backpack_to_cart()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")
    inventory.open_cart()
    cart = CartPage(page, base_url)
    cart.expect_loaded()
    cart.expect_item_count(1)
    expect(page.locator(".inventory_item_name")).to_contain_text("Sauce Labs Backpack")
