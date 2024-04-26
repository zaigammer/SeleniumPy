import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

browserName = "chrome"

if browserName == "chrome":
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # this will automatically download latest version of chrome driver and then launch
elif browserName == "firefox":
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

else:
    print('please pass the correct browser name:' + browserName)
    raise Exception('driver is not found')  # if Browser is not found then it throw exception

driver.implicitly_wait(5)
driver.get("https://app.hubspot.com/login")
driver.find_element(By.ID, 'username').send_keys("merchantmt5@gmail.com")
driver.find_element(By.ID, 'password').send_keys("Admin@123")
driver.find_element(By.ID, 'loginBtn').click()

print(driver.title)

time.sleep(3)
# driver.quit()
