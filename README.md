
# Selenium User Management Automation

This project automates the user management functionality of the OrangeHRM system. It performs tasks such as logging into the system, adding a new user, validating the addition of the user, and more using Selenium WebDriver with Python.

## Project Setup

### Prerequisites

- Python 3.13 or later
- ChromeDriver (or another WebDriver for your preferred browser)
- Selenium
- pytest for testing

### Installation

1. **Clone the repository:**

   Clone the repository to your local machine using:
   ```bash
   cd selenium-user-management
   ```

2. **Create a virtual environment:**

   For isolated Python dependencies, it's best to create a virtual environment:
   ```bash
   python -m venv env
   ```

3. **Activate the virtual environment:**

   On Windows:
   ```bash
   .\env\Scripts\activate
   ```

   On macOS/Linux:
   ```bash
   source env/bin/activate
   ```

4. **Install dependencies:**

   Install the necessary Python packages by running:
   ```bash
   pip install -r requirements.txt
   ```

   `requirements.txt` includes the following dependencies:
   - `selenium`
   - `pytest`
   - `pytest-selenium` (for running Selenium tests)

### Configuration

1. **ChromeDriver**:
   - Download ChromeDriver from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) (ensure the version matches your Chrome version).
   - Make sure the `chromedriver.exe` file is either placed in the project folder or added to your system’s PATH.

2. **OrangeHRM Login Credentials**:
   The login credentials are stored in the test script:
   ```python
   USER_NAME = "Admin"
   PASSWORD = "admin123"
   ```

   These credentials are used to log in to the OrangeHRM demo system.

## Test Structure

### `test_add_user.py`

This script contains test cases for adding and validating a user:

- **`test_login`**: Logs in to the OrangeHRM system.
- **`go_to_add_user_page`**: Navigates to the Add User page.
- **`add_user`**: Adds a user to the system.
- **`test_add_and_validate_user`**: Tests the complete process of logging in, adding a user, and validating that the user is added.

### Example Test Flow

1. **Login**: Logs into the system using predefined credentials (`Admin` / `admin123`).
2. **Navigate to Admin**: The test navigates to the "Add User" page using the URL `https://opensource-demo.orangehrmlive.com/web/index.php/admin/saveSystemUser`.
3. **Add User**: A new user is created with the provided details (`testUser1`, role as `Admin`, and status as `Enabled`).
4. **Validate User**: After adding the user, the script checks if the new user appears in the user list.

## Running the Tests

You can run the tests with the following command:

```bash
pytest test_add_user.py
```

### Test Output

During test execution, you will see logs indicating the status of the test case. If the test fails, the system will automatically capture a screenshot to assist in debugging.

## Troubleshooting

### Timeout Errors

- If the tests fail with a `TimeoutException`, it means that Selenium was unable to find an element within the given time. To resolve this, try:
  - Increasing the timeout in the `WebDriverWait` function.
  - Ensuring that the correct element locators are used (inspect the page's source code for accurate locators).

### Common Issues

- **WebDriver Version**: Ensure that the version of `chromedriver.exe` matches the version of Google Chrome installed on your system.
- **Network Connection**: Slow network connections may cause delays in page load times. Consider increasing the `implicitly_wait()` or `WebDriverWait()` durations.

## Conclusion

This repository contains an automated Selenium test suite for managing users within the OrangeHRM system. It supports logging in, adding new users, and validating those users via the web interface.

