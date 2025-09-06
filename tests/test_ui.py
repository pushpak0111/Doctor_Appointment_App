import subprocess
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_login_page():
    # Start Flask app
    flask_process = subprocess.Popen(["python", "app.py"])
    time.sleep(3)  # Wait for server to start

    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5000/")

    # Check if Login page loaded
    assert "Login" in driver.page_source

    driver.quit()
    flask_process.terminate()
