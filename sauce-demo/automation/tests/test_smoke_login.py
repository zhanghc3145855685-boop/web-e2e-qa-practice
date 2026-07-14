from playwright.sync_api import Page, expect

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

PASSWORD = "secret_sauce"


def test_smoke_valid_login_enters_inventory(page: Page, base_url: str) -> None:
    """4.2.1 正确登录进入商品页"""
    LoginPage(page, base_url).login("standard_user", PASSWORD)
    InventoryPage(page, base_url).expect_loaded()


def test_smoke_wrong_password_shows_error(page: Page, base_url: str) -> None:
    """4.2.2 错误密码登录失败并出现错误提示"""
    login = LoginPage(page, base_url)
    login.login("standard_user", "wrong_password")
    login.expect_still_on_login()
    message = login.error_message()
    assert "Username and password do not match" in message


def test_smoke_locked_out_user_cannot_login(page: Page, base_url: str) -> None:
    """4.2.3 locked 用户无法登录"""
    login = LoginPage(page, base_url)
    login.login("locked_out_user", PASSWORD)
    login.expect_still_on_login()
    message = login.error_message()
    assert "locked out" in message.lower()
    expect(page.locator(".title")).to_have_count(0)
