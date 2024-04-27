from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())  # launch browser
driver.maximize_window()
#
# driver.delete_all_cookies()
driver.implicitly_wait(10)
driver.get("https://www.freshworks.com/")
print(driver.title)

headerElement = driver.find_element(By.TAG_NAME, 'h1')
print(headerElement.text)

# Get Total Links count

linksList = driver.find_elements(By.TAG_NAME, 'a')
print(len(linksList))

ImageList = driver.find_elements(By.TAG_NAME, 'img')
print(len(ImageList))
