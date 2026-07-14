from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page, base_url: str = "https://www.saucedemo.com") -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")

    def expect_url_contains(self, fragment: str) -> None:
        expect(self.page).to_have_url(f"**{fragment}**")
