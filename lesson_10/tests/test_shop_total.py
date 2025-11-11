import allure
from selenium import webdriver
from lesson_10.pages.login_page import LoginPage
from lesson_10.pages.inventory_page import InventoryPage
from lesson_10.pages.cart_page import CartPage
from lesson_10.pages.checkout_page import CheckoutPage


@allure.title("Проверка суммы заказа в магазине SauceDemo")
@allure.description(
    "Тест проверяет, что итоговая сумма заказа корректна после "
    "добавления нескольких товаров."
)
@allure.feature("Интернет-магазин")
@allure.severity(allure.severity_level.NORMAL)
def test_shop_total():
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        driver.get("https://www.saucedemo.com/")

        with allure.step("Авторизация на сайте"):
            login_page = LoginPage(driver)
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()

        with allure.step("Добавление товаров в корзину"):
            inventory_page = InventoryPage(driver)
            items = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]
            for item in items:
                inventory_page.add_to_cart(item)
            inventory_page.go_to_cart()

        with allure.step("Переход к оформлению заказа"):
            cart_page = CartPage(driver)
            cart_page.click_checkout()

        with allure.step("Заполнение формы оформления заказа"):
            checkout_page = CheckoutPage(driver)
            checkout_page.fill_form(
                first_name="Иван",
                last_name="Иванов",
                postal_code="12345"
            )

        with allure.step("Проверка итоговой суммы заказа"):
            total = checkout_page.get_total()
            expected_total = 129.97
            assert total == expected_total, (
                f"Expected {expected_total}, got {total}"
            )

    finally:
        driver.quit()
