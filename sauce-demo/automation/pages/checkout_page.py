from playwright.sync_api import expect

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    def fill_info(self, first: str, last: str, postal: str) -> None:
        self.page.locator("[data-test='firstName']").fill(first)
        self.page.locator("[data-test='lastName']").fill(last)
        self.page.locator("[data-test='postalCode']").fill(postal)

    def continue_to_overview(self) -> None:
        self.page.locator("[data-test='continue']").click()

    def finish(self) -> None:
        self.page.locator("[data-test='finish']").click()

    def expect_complete(self) -> None:
        expect(self.page).to_have_url(f"{self.base_url}/checkout-complete.html")
        expect(self.page.locator(".complete-header")).to_have_text("Thank you for your order!")
