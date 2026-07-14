from playwright.sync_api import expect

from pages.base_page import BasePage


class CartPage(BasePage):
    def expect_loaded(self) -> None:
        expect(self.page).to_have_url(f"{self.base_url}/cart.html")

    def expect_item_count(self, count: int) -> None:
        expect(self.page.locator(".cart_item")).to_have_count(count)

    def checkout(self) -> None:
        self.page.locator("[data-test='checkout']").click()
