from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def login(config):
    options = Options()
    driver = webdriver.Chrome(options=options)
    driver.get(config["login_url"])
    wait = WebDriverWait(driver, 20)

    for f in ["username", "id", "password"]:
        field_name = config["selectors"][f]
        # field = wait.until(EC.presence_of_element_located((By.ID, field_name)))

        field = wait.until(EC.element_to_be_clickable((By.ID, field_name)))
        field.clear()
        field.send_keys(config[f])

    login_btn = wait.until(EC.element_to_be_clickable((By.ID, "loginButton")))
    login_btn.click()

    # Wait for login to complete - URL should change from login page
    wait.until(EC.url_changes(config["login_url"]))
    time.sleep(2)  # Additional wait for authentication to complete

    return driver
