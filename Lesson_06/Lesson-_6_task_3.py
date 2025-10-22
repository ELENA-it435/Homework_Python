from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)

# Ждём, пока появится третья картинка
third_img = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "img:nth-of-type(3)"))
)

print(third_img.get_attribute("src"))
driver.quit()
