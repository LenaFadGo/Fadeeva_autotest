from selenium import webdriver
import time
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

def test_open_litress():
    driver.get("https://www.litres.ru")
    # time.sleep(12)
    accept_button = driver.find_element(by=By.XPATH, value="//div[text()='Принять']")
    accept_button.click()
    search_string = driver.find_element(By.CSS_SELECTOR, '[data-testid = "search__input"]')
    search_string.send_keys("Пушкин")
    button = driver.find_element(By.XPATH, '//button[@aria-label="Найти "]')
    button.click()
    driver.quit()



















