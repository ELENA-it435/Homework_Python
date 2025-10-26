from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


def test_calc_result():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    )

    driver.find_element(By.ID, "delay").clear()
    driver.find_element(By.ID, "delay").send_keys("45")

    for symbol in ["7", "+", "8", "="]:
        driver.find_element(By.XPATH, f"//span[text()='{symbol}']").click()

    WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(
            (By.CLASS_NAME, "screen"), "15"
        )
    )

    result = driver.find_element(By.CLASS_NAME, "screen").text
    assert result == "15", f"Ожидалось 15, получено {result}"

    driver.quit()
