from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

options = Options()
options.add_argument('--headless')
options.add_argument('window-size=1920x1080')


# driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
web = 'https://www.audible.com/adblbestsellers?ref=a_search_t1_navTop_pl0cg1c0r0&pf_rd_p=1bb99d4d-8ec8-42a3-bb35-704e849c2bc6&pf_rd_r=1Z5AHBSCNHZBW535YGAV&pageLoadId=E6qhmggHrvrE3rpa&creativeId=1642b4d1-12f3-4375-98fa-4938afc1cedc'
time.sleep(1)
driver.get(web)
# driver.maximize_window()

# pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
lastPage = int(pages[-2].text)
currentPage = 1

book_title = []
book_author = []
book_length = []

while currentPage <= lastPage:
    time.sleep(2)
    parentElement = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
    print(parentElement.text)
    products = parentElement.find_elements(By.XPATH, './div/span/ul/li')  # Use find_elements to find multiple elements
    print(products)

    for prod in products:
        book_title.append(prod.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text)
        book_author.append(prod.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text)
        book_length.append(prod.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text)

    currentPage = currentPage + 1
    try:
        nextPage = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        nextPage.click()
    except:
        pass

driver.quit()

# dataframe
df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
df_books.to_csv('data_test.csv', index=False)  # df_books.to_json for json format

# time.sleep(1000)
