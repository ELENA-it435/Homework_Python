from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/ajax")

driver.find_element(By.ID, "ajaxButton").click()
WebDriverWait(driver, 20).until(
    EC.text_to_be_present_in_element(
        (By.CLASS_NAME, "bg-success"), "Data loaded"
    )
)
print(driver.find_element(By.CLASS_NAME, "bg-success").text)
driver.quit()
