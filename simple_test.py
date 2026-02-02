
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.litres.ru/")

driver.find_element(By.XPATH, "//div[text() = 'Пушкин']")


