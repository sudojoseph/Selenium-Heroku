from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

# service = Service(os.environ.get("CHROMEDRIVER_PATH"))
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://google.com")
print(driver.title)
print(driver.title)
print(driver.title)
print(driver.title)
print(driver.title)
print(driver.title)
print(driver.title)

driver.quit()