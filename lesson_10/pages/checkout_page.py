from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:
    """Страница оформления заказа."""

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: экземпляр WebDriver.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_label = (By.CLASS_NAME, "summary_total_label")

    def fill_form(
        self, first_name: str, last_name: str, postal_code: str
    ) -> None:
        """
        Заполняет форму оформления заказа и нажимает кнопку продолжить.

        :param first_name: имя покупателя.
        :param last_name: фамилия покупателя.
        :param postal_code: почтовый индекс.
        """
        self.wait.until(
            EC.visibility_of_element_located(
                self.first_name_input
            )
        ).send_keys(first_name)

        self.wait.until(
            EC.visibility_of_element_located(
                self.last_name_input
            )
        ).send_keys(last_name)

        self.wait.until(
            EC.visibility_of_element_located(
                self.postal_code_input
            )
        ).send_keys(postal_code)

        self.wait.until(
            EC.element_to_be_clickable(
                self.continue_button
            )
        ).click()

    def get_total(self) -> float:
        """
        Получает итоговую сумму заказа.

        :return: сумма заказа (float).
        """
        element = self.wait.until(
            EC.visibility_of_element_located(
                self.total_label
            )
        )
        total_text = element.text
        total_value = total_text.replace("Total: $", "")
        return float(total_value)
