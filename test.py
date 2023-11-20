 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

chrome_driver_path = r"C:\webdrivers\chromedriver.exe"
driver = webdriver.Chrome()

driver.get("https://squareup.com/dashboard/sales/transactions")
location = "Email address"
element = WebDriverWait(driver, 0.5).until(EC.presence_of_element_located((By.XPATH, f"//input[@aria-label = '{location}']")))
time.sleep(0.5)
element.send_keys('bungou stray dogs')
element.send_keys(Keys.ENTER)
time.sleep(0.5)
print("process finished!!!!!!!!!!")
driver.quit()
 
