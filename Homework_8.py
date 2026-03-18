from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()

def test_open_litress():
    driver.get("https://www.litres.ru")
    # time.sleep(12)
    accept_button = driver.find_element(by=By.XPATH, value="//div[text()='Принять']")
    accept_button.click()
    search_string = driver.find_element(By.CSS_SELECTOR, '[data-testid = "search__input"]')
    search_string.send_keys("Пушкин")
    button = driver.find_element(By.XPATH, '//button[text()="Найти"]')
    button.click()
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-testid='search__content--wrapper']")))
    book_titles = driver.find_elements(By.CSS_SELECTOR, '[data-testid = "art__title"]')

    driver.quit()



















