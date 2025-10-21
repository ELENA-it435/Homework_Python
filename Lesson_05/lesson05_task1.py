﻿from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Скрипт нужно запустить вручную 3 раза
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://uitestingplayground.com/classattr")
driver.find_element(By.CSS_SELECTOR, "button.btn-primary").click()
driver.quit()
