from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

# driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
web = ('https://www.audible.com/search')
time.sleep(1)
driver.get(web)
# driver.maximize_window()

parentElement = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
product = parentElement.find_element(By.XPATH, './/li')

print(product.text)
time.sleep(1000)
