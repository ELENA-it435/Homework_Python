from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager


def test_shop_total():
    driver = webdriver.Firefox(
        service=Service(GeckoDriverManager().install())
    )
    wait = WebDriverWait(driver, 20)
    driver.get("https://www.saucedemo.com/")

    wait.until(EC.visibility_of_element_located(
        (By.ID, "user-name")
    )).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    for item_id in [
        "add-to-cart-sauce-labs-backpack",
        "add-to-cart-sauce-labs-bolt-t-shirt",
        "add-to-cart-sauce-labs-onesie"
    ]:
        wait.until(EC.element_to_be_clickable(
            (By.ID, item_id)
        )).click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable(
        (By.ID, "checkout")
    )).click()

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "postal-code": "12345"
    }

    for field_id, value in fields.items():
        wait.until(EC.visibility_of_element_located(
            (By.ID, field_id)
        )).send_keys(value)

    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(EC.visibility_of_element_located(
        (By.CLASS_NAME, "summary_total_label")
    )).text
    assert total_text == "Total: $58.29", (
        f"Ожидалось Total: $58.29, получено {total_text}"
    )

    driver.quit()
