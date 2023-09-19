from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd
import time

# driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
web = 'https://www.audible.com/search'
time.sleep(1)
driver.get(web)

parentElement = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
products = parentElement.find_elements(By.XPATH, './/li')  # Use find_elements to find multiple elements

book_title = []
book_author = []
book_length = []

for prod in products:
    book_title.append(prod.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
    book_author.append(prod.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
    book_length.append(prod.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

driver.quit()

# dataframe
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('data.csv', index=False)

# time.sleep(1000)
