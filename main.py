from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

driver.get("https://www.google.com")
print(driver.title)