import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(ChromeDriverManager().install())  #launch browser
driver.implicitly_wait(10)

print(driver.title)

driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
username_url = driver.find_element(By.ID, 'Form_getForm_subdomain')
firstname = driver.find_element(By.ID, 'Form_getForm_Name')
Email_id = driver.find_element(By.ID, 'Form_getForm_Email')

username_url.send_keys("Automation Labs")
firstname.send_keys("Automation")
Email_id.send_keys("aut@gmail.com")
