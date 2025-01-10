import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://opensource-demo.orangehrmlive.com"
USER_NAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Replace with your browser driver
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(f"{BASE_URL}/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_login(setup):
    driver = setup

    try:
        # Wait for the login page to load
        print("Waiting for the login page to load...")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))

        # Enter login credentials
        print("Entering username...")
        driver.find_element(By.NAME, "username").send_keys(USER_NAME)
        print("Entering password...")
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        print("Clicking login button...")
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Validate successful login
        print("Validating login...")
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Admin']")))
        print("Admin menu located. Login successful.")

    except Exception as e:
        print(f"Test failed: {e}")
        print(f"Current URL: {driver.current_url}")
        driver.save_screenshot("debug_login_failure.png")
        raise
