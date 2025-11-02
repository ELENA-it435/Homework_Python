from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
    Класс для работы с онлайн калькулятором на странице
    https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html
    """

    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы калькулятора.

        :param driver: объект WebDriver
        """
        self.driver: WebDriver = driver
        self.url: str = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self) -> None:
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(self.url)

    def set_delay(self, value: str) -> None:
        """
        Устанавливает задержку для калькулятора.

        :param value: значение задержки в миллисекундах
        """
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(value)

    def click_button(self, symbol: str) -> None:
        """
        Нажимает кнопку на калькуляторе по символу.

        :param symbol: символ кнопки ('1', '2', '+', '=', и т.д.)
        """
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{symbol}']"
        ).click()

    def wait_for_result(self, expected_text: str, timeout: int = 50) -> None:
        """
        Ждет, пока на экране калькулятора появится ожидаемый результат.

        :param expected_text: ожидаемый текст на экране
        :param timeout: время ожидания в секундах
        """
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(
                self.screen,
                expected_text
            )
        )

    def get_result(self) -> str:
        """
        Возвращает текст с экрана калькулятора.

        :return: текст с экрана калькулятора
        """
        return self.driver.find_element(*self.screen).text
