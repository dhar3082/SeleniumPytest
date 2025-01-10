import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Constants for login credentials and base URL
BASE_URL = "https://opensource-demo.orangehrmlive.com"
USER_NAME = "Admin"
PASSWORD = "admin123"

@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # Replace with your browser driver if necessary
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(f"{BASE_URL}/web/index.php/auth/login")
    yield driver
    driver.quit()

def login(driver):
    """Login function to log into the system."""
    try:
        # Wait for the login page to load
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "username")))

        # Enter login credentials
        driver.find_element(By.NAME, "username").send_keys(USER_NAME)
        driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        driver.find_element(By.XPATH, '//button[@type="submit"]').click()

        # Wait for the Admin menu to appear after successful login
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//span[text()='Admin']")))

    except Exception as e:
        print(f"Login failed: {e}")
        driver.save_screenshot("debug_login_failure.png")
        raise

def go_to_add_user_page(driver):
    """Navigate to the 'Add User' page."""
    driver.get(f"{BASE_URL}/web/index.php/admin/saveSystemUser")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "systemUser[userName]")))

def add_user(driver, username, role, status):
    """Function to add a user from the Add User page."""
    # Fill in the user details
    driver.find_element(By.NAME, "systemUser[userName]").send_keys(username)
    driver.find_element(By.NAME, "systemUser[password]").send_keys("Test@123")
    driver.find_element(By.NAME, "systemUser[confirmPassword]").send_keys("Test@123")
    
    # Select the role (e.g., Admin or ESS)
    role_dropdown = driver.find_element(By.NAME, "systemUser[role]")
    role_dropdown.click()
    role_dropdown.send_keys(role)
    
    # Select the status (e.g., Enabled or Disabled)
    status_dropdown = driver.find_element(By.NAME, "systemUser[status]")
    status_dropdown.click()
    status_dropdown.send_keys(status)

    # Click "Save" to add the user
    driver.find_element(By.ID, "btnSave").click()

def test_add_and_validate_user(setup):
    """Test case to add and validate a user."""
    driver = setup
    login(driver)

    # Go to Add User page
    go_to_add_user_page(driver)

    # Add user
    add_user(driver, "testUser1", "Admin", "Enabled")
    
    # Validate if the user is added (search by username)
    driver.get(f"{BASE_URL}/web/index.php/admin/viewSystemUsers")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "searchSystemUser_userName")))
    driver.find_element(By.ID, "searchSystemUser_userName").send_keys("testUser1")
    driver.find_element(By.ID, "searchBtn").click()
    
    # Validate that the user appears in the search results
    assert "testUser1" in driver.page_source

