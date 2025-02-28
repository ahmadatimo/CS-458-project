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

time.sleep(2)

# assign the elements:
email = driver.find_element(By.NAME, "email")
password = driver.find_element(By.NAME, "password")
login = driver.find_element(By.NAME, "submit")

# write email:
email.send_keys("lupin@hogwarts.com")
time.sleep(2)

password.send_keys("eatCh0lklate")
time.sleep(2)

login.send_keys(Keys.ENTER)
time.sleep(2)


password.clear()
time.sleep(2)


password.send_keys("eatCh0lklate")
time.sleep(2)

login.send_keys(Keys.ENTER)
time.sleep(2)


password.clear()
time.sleep(2)

password.send_keys("eatCh0lklate")
time.sleep(2)

login.send_keys(Keys.ENTER)
time.sleep(2)


password.clear()
time.sleep(2)

password.send_keys("eatCh0lklate")
time.sleep(2)

login.send_keys(Keys.ENTER)
time.sleep(2)


password.clear()
time.sleep(2)

password.send_keys("eatCh0lklate")
time.sleep(2)

login.send_keys(Keys.ENTER)
time.sleep(2)


password.clear()
time.sleep(2)

password.send_keys("eatCh0lklate")
time.sleep(2)

login.send_keys(Keys.ENTER)
time.sleep(2)

driver.quit()

