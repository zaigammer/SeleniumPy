import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("http://www.google.com")
print(driver.title)

driver.find_element(By.NAME, 'q').send_keys("Python automation")
opionslist = driver.find_elements(By.XPATH, '//div[@id="Alh6id"]//li')  # getting mulitiple data in list
print(len(opionslist))

for ele in opionslist:  # Using for loop and print lenght of list
    print(ele.text)
    if ele.text == 'python automation testing':
        # once the following text is visibale then click on it
        ele.click()
        break

time.sleep(3)
driver.quit()