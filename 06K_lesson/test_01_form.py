from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submit():
    service = Service(
        "C:\\Users\\rados\\Downloads\\edgedriver_win64\\msedgedriver.exe"
    )
    driver = webdriver.Edge(service=service)
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
    )

    data = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+798589999"
    }

    for name, value in data.items():
        driver.find_element(By.NAME, name).send_keys(value)

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input.is-valid, input.is-invalid")
        )
    )

    zip_class = driver.find_element(By.NAME, "zip-code").get_attribute("class")
    assert "is-invalid" in zip_class

    for name in data.keys():
        field_class = driver.find_element(By.NAME, name).get_attribute("class")
        assert "is-valid" in field_class

    driver.quit()
