from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_username(self, username):
        field = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "user-name")
        ))
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "password")
        ))
        field.send_keys(password)

    def click_login(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "login-button")
        ))
        btn.click()


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_to_cart(self, item):
        xpath = (
            f"//div[text()='{item}']/ancestor::div[@class='inventory_item']"
            "//button"
        )
        btn = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        btn.click()

    def go_to_cart(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "shopping_cart_container")
        ))
        btn.click()


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        btn = self.wait.until(EC.element_to_be_clickable(
            (By.ID, "checkout")
        ))
        btn.click()


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first, last, postal):
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, "first-name")
        )).send_keys(first)
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, "last-name")
        )).send_keys(last)
        self.wait.until(EC.visibility_of_element_located(
            (By.ID, "postal-code")
        )).send_keys(postal)
        self.wait.until(EC.element_to_be_clickable(
            (By.ID, "continue")
        )).click()

    def get_total(self):
        text = self.wait.until(EC.visibility_of_element_located(
            (By.CLASS_NAME, "summary_total_label")
        )).text
        return float(text.replace("Total: $", ""))


def test_shop_total():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.saucedemo.com/")

    login = LoginPage(driver)
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login()

    inventory = InventoryPage(driver)
    for item in [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]:
        inventory.add_to_cart(item)
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.click_checkout()

    checkout = CheckoutPage(driver)
    first_name = "Иван"
    last_name = "Петров"
    postal_code = "12345"
    checkout.fill_form(first_name, last_name, postal_code)

    total = checkout.get_total()
    driver.quit()

    assert total == 58.29
