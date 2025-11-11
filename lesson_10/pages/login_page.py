from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    """Страница авторизации на сайте."""

    def __init__(self, driver):
        """
        Инициализация страницы логина.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        :param username: имя пользователя.
        """
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.username_input)
        )
        username_field.send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль пользователя.

        :param password: пароль пользователя.
        """
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.password_input)
        )
        password_field.send_keys(password)

    def click_login(self) -> None:
        """Нажимает кнопку входа."""
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.login_button)
        )
        login_btn.click()
