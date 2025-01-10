import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    @pytest.fixture(scope="class", autouse=True)  # Automatically use the setup fixture for the class
    def setup(self, request):
        print("Setting up the browser...")
        chrome_driver_path = "C:\\Users\\cliff\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe"
        service = Service(chrome_driver_path)  # Use Service to specify the driver path
        driver = webdriver.Chrome(service=service)
        driver.maximize_window()
        print("Browser launched and maximized.")
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers")
        print("Navigated to the login page.")
        request.cls.driver = driver  # Attach the driver to the test class
        yield
        print("Closing the browser...")
        driver.quit()
        print("Browser closed.")

    def test_login(self):
        # Locate login fields and button
        print("Locating username field...")
        username_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        print("Username field located.")

        print("Locating password field...")
        password_field = self.driver.find_element(By.NAME, "password")
        print("Password field located.")

        print("Locating login button...")
        login_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        print("Login button located.")

        # Perform login
        print("Entering credentials...")
        username_field.send_keys("Admin")
        password_field.send_keys("admin123")
        print("Credentials entered. Clicking login button...")
        login_button.click()

        # Validate successful login by checking the presence of a specific element
        print("Waiting for Admin tab to appear...")
        admin_tab = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/web/index.php/admin/viewAdminModule']"))
        )
        assert admin_tab.is_displayed()
        print("Login successful. Admin tab is displayed.")
