"""AttendX - Attendance marking test.
Checks that a teacher can mark a student present and see a success message."""
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "http://localhost:3000"  # change to the AttendX URL


def test_mark_attendance():
    driver = webdriver.Chrome()
    try:
        driver.get(BASE_URL + "/login")
        driver.find_element(By.ID, "username").send_keys("teacher01")
        driver.find_element(By.ID, "password").send_keys("password123")
        driver.find_element(By.ID, "login-btn").click()

        driver.get(BASE_URL + "/attendance")
        driver.find_element(By.ID, "present-student-1").click()
        driver.find_element(By.ID, "save-attendance").click()
        message = driver.find_element(By.ID, "success-msg").text
        assert "saved" in message.lower(), "Attendance was not saved"
        print("PASS: attendance marked")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_mark_attendance()
