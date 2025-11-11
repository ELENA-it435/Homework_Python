from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CartPage:
    """Страница корзины."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")

    def click_checkout(self) -> None:
        self.wait.until(
            EC.visibility_of_element_located(self.cart_items)
        )
        button = self.wait.until(
            EC.presence_of_element_located(self.checkout_button)
        )
        self.driver.execute_script("arguments[0].click();", button)
