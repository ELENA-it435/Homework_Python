from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Важно: скрипт нужно запустить вручную 3 раза подряд
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/dynamicid")
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
driver.quit()
