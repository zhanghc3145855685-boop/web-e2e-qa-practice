"""Pytest fixtures for Sauce Demo smoke automation."""
from __future__ import annotations

from pathlib import Path

import pytest
from playwright.sync_api import Page

BASE_URL = "https://www.saucedemo.com"
SCREENSHOT_DIR = Path(__file__).resolve().parent / "screenshots"
REPORT_DIR = Path(__file__).resolve().parent / "reports"


@pytest.fixture(scope="session")
def base_url() -> str:
    return BASE_URL


@pytest.fixture(autouse=True)
def _ensure_dirs() -> None:
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    REPORT_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(autouse=True)
def open_login_page(page: Page, base_url: str) -> None:
    """Each test starts on the Sauce Demo login page."""
    page.set_default_timeout(15_000)
    page.goto(f"{base_url}/")


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    """On failure, save an extra screenshot under screenshots/."""
    outcome = yield
    report = outcome.get_result()
    if report.when != "call" or not report.failed:
        return
    page = item.funcargs.get("page")
    if page is None:
        return
    path = SCREENSHOT_DIR / f"{item.name}.png"
    try:
        page.screenshot(path=str(path), full_page=True)
        report.sections.append(("Failure screenshot", str(path)))
    except Exception as exc:  # noqa: BLE001 — best-effort artifact
        report.sections.append(("Failure screenshot error", str(exc)))
