from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(browser):
    browser.get("https://www.google.com")
    assert "Google" in browser.title
    search_box = browser.find_element(By.NAME, "q")
    search_box.send_keys("GitHub Copilot")
    search_box.submit()
    results = browser.find_elements(By.CSS_SELECTOR, "h3")
    assert len(results) > 0