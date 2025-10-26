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
    driver.get("https://www.saucedemo.com/")
    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    ).send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    wait.until(
        EC.element_to_be_clickable(
            (By.ID, "add-to-cart-sauce-labs-backpack")
        )
    ).click()
    driver.find_element(
        By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
    ).click()
    driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()

    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()

    wait.until(
        EC.visibility_of_element_located((By.ID, "first-name"))
    ).send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()

    total_text = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )
    ).text

    if total_text == "Total: $58.29":
        print(f"✅ Тест пройден: {total_text}")
    else:
        print(
            f"❌ Тест не пройден: ожидалось $58.29, получено "
            f"{total_text}"
        )
        assert False

    driver.quit()


if __name__ == "__main__":
    test_shop_total()
