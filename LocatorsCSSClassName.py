from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())  # launch browser
driver.maximize_window()
#
# driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.get("https://app.hubspot.com/login")
print(driver.title)

# driver.find_element(By.CSS_SELECTOR, '#username').send_keys("Automation@yopmail.com")
# driver.find_element(By.CLASS_NAME, 'login-password').send_keys("Test@123")
# driver.find_element(By.CLASS_NAME, 'login-submit').click()

driver.find_element(By.LINK_TEXT, 'Forgot my password').click()

time.sleep(3)
