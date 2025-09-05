from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://127.0.0.1:5000/")

# Example test: Check login page title
assert "Login" in driver.page_source

driver.quit()
h