"""AttendX - Login test.
Checks that a valid user can log in and reach the dashboard."""
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:3000"  # change to the AttendX URL
USERNAME = "teacher01"
PASSWORD = "password123"


def test_valid_login():
    driver = webdriver.Chrome()
    try:
        driver.get(BASE_URL + "/login")
        driver.find_element(By.ID, "username").send_keys(USERNAME)
        driver.find_element(By.ID, "password").send_keys(PASSWORD)
        driver.find_element(By.ID, "login-btn").click()
        assert "dashboard" in driver.current_url.lower(), "Login did not reach dashboard"
        print("PASS: valid login")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_valid_login()
