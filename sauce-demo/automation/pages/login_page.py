from playwright.sync_api import expect

from pages.base_page import BasePage


class LoginPage(BasePage):
    def fill_credentials(self, username: str, password: str) -> None:
        self.page.locator("#user-name").fill(username)
        self.page.locator("#password").fill(password)

    def submit(self) -> None:
        self.page.locator("#login-button").click()

    def login(self, username: str, password: str) -> None:
        self.fill_credentials(username, password)
        self.submit()

    def error_message(self) -> str:
        loc = self.page.locator("[data-test='error']")
        expect(loc).to_be_visible()
        return loc.inner_text()

    def expect_still_on_login(self) -> None:
        expect(self.page.locator("#login-button")).to_be_visible()
        expect(self.page).not_to_have_url("**/inventory.html")
