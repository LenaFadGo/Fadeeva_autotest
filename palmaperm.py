from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options

# options = Options()
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--disable-site-isolation-trials")
# options.add_argument("--ignore-certificate-errors")
# options.add_argument("--allow-insecure-localhost")
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)

# driver.get ("https://palmaperm.ru/")
# element = driver.find_element(By.XPATH, "//span[text()='Корея']")
# element.click()

def test_open_podrygka():
    driver.get("https://www.podrygka.ru/")
    accept_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[text()='Подарочные карты']")))
    accept_button.click()

