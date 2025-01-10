# test_delete_user.py
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

def test_delete_user(setup):
    driver = setup

    # Perform login actions
    driver.find_element(By.NAME, "username").send_keys(USER_NAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, '//button[@type="submit"]').click()

    # Navigate to User Management page
    driver.get(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")

    # Search for testUser2
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("testUser2")
    driver.find_element(By.ID, "searchBtn").click()

    # Delete the user
    driver.find_element(By.XPATH, "//*[text()='testUser2']/../..//input").click()
    driver.find_element(By.ID, "btnDelete").click()
    driver.find_element(By.ID, "dialogDeleteBtn").click()

    # Validate the user is deleted
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("testUser2")
    driver.find_element(By.ID, "searchBtn").click()
    assert "No Records Found" in driver.page_source
    print("Delete user test passed.")