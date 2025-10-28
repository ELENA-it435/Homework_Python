from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item_name):
        button = (By.XPATH, f"//div[text()='{item_name}']/ancestor::div[@class='inventory_item']//button")
        self.wait.until(EC.element_to_be_clickable(button)).click()

    def go_to_cart(self):
        cart = (By.ID, "shopping_cart_container")
        self.wait.until(EC.element_to_be_clickable(cart)).click()
