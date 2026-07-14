from playwright.sync_api import expect

from pages.base_page import BasePage


class InventoryPage(BasePage):
    def expect_loaded(self) -> None:
        expect(self.page).to_have_url(f"{self.base_url}/inventory.html")
        expect(self.page.locator(".title")).to_have_text("Products")

    def add_backpack_to_cart(self) -> None:
        self.page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()

    def open_cart(self) -> None:
        self.page.locator(".shopping_cart_link").click()

    def cart_badge_count(self) -> str:
        return self.page.locator(".shopping_cart_badge").inner_text()
