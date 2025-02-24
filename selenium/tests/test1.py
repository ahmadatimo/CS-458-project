from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Create a WebDriver service
service = Service(executable_path="chromedriver.exe")

# Start Chrome WebDriver with the service
driver = webdriver.Chrome(service=service)  # ✅ 'service' should be lowercase

# Open the frontend (Vite default port)
driver.get("http://localhost:3000")

# appreciate the page
time.sleep(1)

# add a name
email = driver.find_element(By.NAME, "email")
email.send_keys("test@example.com")

time.sleep(1)

# add a password
password = driver.find_element(By.NAME, "password")
password.send_keys("123456")

# login
login = driver.find_element(By.NAME, "Submit")
login.send_keys(Keys.ENTER)

time.sleep(2)

# Close the browser
driver.quit()
