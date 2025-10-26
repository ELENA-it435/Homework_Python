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

    driver.find_element(By.NAME, "first-name").send_keys("Иван")
    driver.find_element(By.NAME, "last-name").send_keys("Петров")
    driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    driver.find_element(By.NAME, "phone").send_keys("+798589999")

    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".alert-success"))
    )

    print("✅ Тест успешно выполнен!")

    driver.quit()


if __name__ == "__main__":
    test_form_submit()
