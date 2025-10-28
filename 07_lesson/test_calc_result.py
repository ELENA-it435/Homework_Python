import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


@pytest.fixture()
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calc_result(driver):
    page = CalculatorPage(driver)
    page.open()
    page.set_delay("45")

    for symbol in ["7", "+", "8", "="]:
        page.click_button(symbol)

    page.wait_for_result("15")
    result = page.get_result()

    assert result == "15", f"Ожидалось 15, получено {result}"
