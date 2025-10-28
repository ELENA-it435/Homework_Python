from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = (
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )
        self.delay_input = (By.ID, "delay")
        self.screen = (By.CLASS_NAME, "screen")

    def open(self):
        self.driver.get(self.url)

    def set_delay(self, value: str):
        delay = self.driver.find_element(*self.delay_input)
        delay.clear()
        delay.send_keys(value)

    def click_button(self, symbol: str):
        self.driver.find_element(
            By.XPATH,
            f"//span[text()='{symbol}']"
        ).click()

    def wait_for_result(self, expected_text: str, timeout: int = 50):
        WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(self.screen, expected_text)
        )

    def get_result(self):
        return self.driver.find_element(*self.screen).text
