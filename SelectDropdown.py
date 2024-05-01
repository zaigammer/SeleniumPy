from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(ChromeDriverManager().install())  # launch browser
driver.maximize_window()

driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/30-day-free-trial/")
print(driver.title)


# Created one generic method with def keyword , select_value method name
def select_values(element, value):
    select = Select(element)
    # Create a Select object to interact with the dropdown element
    select.select_by_visible_text(value)
    # Select the option in the dropdown based on the visible text


Country = driver.find_element(By.ID, 'Form_getForm_Country')
# induct = driver.find_element(By.ID, 'Form_getForm_Industry')

# select_values(Country, 'Australia')
# select = Select(Country)
# select.select_by_visible_text('Australia')
# select.select_by_index(7)
# select.select_by_value('Brazil')

# print(select.is_multiple)  # from this you can identify if dropdown is multiple select or not

# Select the dropdown without using select class
Count_list = driver.find_elements(By.XPATH, '//select[@id="Form_getForm_Country"]/option')
print(len(Count_list))
for ele in Count_list:
    print(ele.text)
    if ele.text == 'Australia':
        ele.click()
        break
