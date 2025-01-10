# test_reset_search.py
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://opensource-demo.orangehrmlive.com"
USER_NAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.get(f"{BASE_URL}/web/index.php/auth/login")
    yield driver
    driver.quit()

def test_reset_search(setup):
    driver = setup

    # Perform login actions
    driver.find_element(By.NAME, "username").send_keys(USER_NAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Navigate to User Management page
    driver.get(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")

    # Perform a search
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("testUser1")
    driver.find_element(By.ID, "searchBtn").click()

    # Reset the search
    driver.find_element(By.ID, "resetBtn").click()

    # Validate that the search fields are cleared
    search_input = driver.find_element(By.ID, "searchSystemUser_userName")
    assert search_input.get_attribute("value") == ""
    print("Reset search test passed.")
